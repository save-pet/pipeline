import os
import time
import math
import requests
# from twilio.rest import Client
from datetime import datetime, timedelta
from pymongo import MongoClient
from dotenv import load_dotenv
from pprint import pprint
from pytz import timezone
from tqdm import tqdm

def get_db(database_name):
    mongodb_URL = os.environ.get('mongodbURL')
    client = MongoClient(mongodb_URL)
    db = getattr(client, database_name)
    return db

def get_url(API_Key, date, page_number = 1):
    URL = f"http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?bgnde={date}&numOfRows=1000&pageNo={page_number}&serviceKey={API_Key}&_type=json"
    return URL

def get_requests_params(key, days_ago):
    API_Key = os.environ.get(key)
    date = (datetime.now(timezone('Asia/Seoul'))- timedelta(days_ago)).strftime('%Y%m%d')
    return API_Key, date

def get_total_count_pages(API_Key, date):
    URL = get_url(API_Key, date)
    rq = requests.get(URL)
    data = rq.json()
    animal_info_totalCount = data['response']['body']['totalCount']
    animal_info_totalPages = math.ceil(animal_info_totalCount/1000)
    return animal_info_totalCount, animal_info_totalPages

def get_info_list_by_page(API_Key, date, page_number):
    print_current_page = f'''current page : {page_number}\n'''
    print(print_current_page)
    post_log("<br>"+ print_current_page)
    with open('/var/www/html/index.html', 'a', encoding="utf-8") as html_file:
            html_file.write("|"*100+f" (if page No.{page_number} 100%) <br>")
    
    URL = get_url(API_Key, date, page_number)
    rq = requests.get(URL)
    data = rq.json()
    info_list = data['response']['body']['items']['item']
    return info_list

def get_shelter_info(db):
    shelter_info_list = list(db.careRegNo.find())
    shelter_info_dict = {shelter_info['careNm'] : shelter_info['careRegNo'] for shelter_info in shelter_info_list}
    return shelter_info_dict

def is_good_data(data_dict, key):
    result = ""
    try:
        result = data_dict[key]
    except:
        # print(key)
        pass
    return result

def address2coord(address):
    preprocess_address = address.split("(")[0]
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"KakaoAK {os.environ.get('KAKAO_REST_API_KEY')}",
        'Host': 'dapi.kakao.com',
    }
    URL = f"https://dapi.kakao.com/v2/local/search/address.json?query={preprocess_address}"

    rq = requests.get(URL, headers=headers)
    data = rq.json()

    if ('documents' not in data) or (len(data['documents'])==0):
        # pprint(data)
        # print(address)
        # print("address2coord Error")
        return 0
        
    lng = float(data['documents'][0]['address']['x']) # 경도 127.XX
    lat = float(data['documents'][0]['address']['y']) # 위도 36.xx
    return {"latitude": lat, "longitude": lng}

def place2coord(place):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"KakaoAK {os.environ.get('KAKAO_REST_API_KEY')}",
        'Host': 'dapi.kakao.com',
    }
    URL = f"https://dapi.kakao.com/v2/local/search/keyword.json?query={place}"

    rq = requests.get(URL, headers=headers)
    data = rq.json()
    if ('documents' not in data) or (len(data['documents'])==0):
        return 0
    return data['documents']

def preprocessing_data(place):
    address = place.split()
    preprocess_data = [elem for elem in address if '동' in elem or '리' in elem or '면' in elem or '읍' in elem or '시' in elem]
    if len(preprocess_data)==0:
        return 0
    return preprocess_data[-1]

def get_center_coord(data):
    cunsum_dict = {"lat": 0, "lng": 0}
    for elem in data:
        cunsum_dict['lat'] += float(elem['y'])
        cunsum_dict['lng'] += float(elem['x'])
    result = {"latitude": float(cunsum_dict['lat'])/len(data), "longitude": float(cunsum_dict['lng'])/len(data)}
    # print(result)
    return result

def get_coord(place, shelter_address):
    data = place2coord(place)
    if data == 0:
        data = place2coord(preprocessing_data(place))
        if data == 0:
            coord = address2coord(shelter_address)
            if coord == 0:
                return {"latitude": 37.23988837533657, "longitude": 131.8719452704162}
            else:
                return coord
        else: 
            return get_center_coord(data)
    else: 
        return get_center_coord(data)

def post_log(log):
    try:
        with open('/var/www/html/index.html', 'a', encoding="utf-8") as html_file:
            time = datetime.now(timezone('Asia/Seoul')).strftime('[%Y%m%d %H:%M:%S] ')
            html_file.write(time + log + "<br>")
    except:
        pass
def post_progressbar(bar):
    try:
        with open('/var/www/html/index.html', 'a', encoding="utf-8") as html_file:
            html_file.write(bar)
    except:
        pass

def get_current_count_by_carecode(result):
    count_dict = {}
    for result_dict in result:
        care_code = result_dict['careCode']
        count_dict[care_code] = count_dict.setdefault(care_code, 0) + 1
    return count_dict

def get_previous_count_by_carecode(care_code):
    load_dotenv()
    headers = {
        'Content-Type': 'application/json',
        'authorization': f"Bearer {os.environ.get('SERVER_TOKEN')}",
    }
    URL = f"http://{os.environ.get('DOMAIN')}:5000/api/rescue/care-code/count/{care_code}"
    rq = requests.get(URL, headers=headers)
    data = rq.json()
    return data

def get_target_shelter(current_count_by_carecode):
    target_shelter = []
    for care_code, currrent_count in current_count_by_carecode.items():
        previous_count = get_previous_count_by_carecode(care_code)
        # print("previous_count")
        # print(previous_count)
        if currrent_count != previous_count:
            target_shelter.append(care_code)
    return target_shelter

def get_shelter_name_by_carecode(careCode):
    load_dotenv()
    headers = {
        'Content-Type': 'application/json',
        'authorization': f"Bearer {os.environ.get('SERVER_TOKEN')}",
    }
    URL = f"http://{os.environ.get('DOMAIN')}:5000/api/shelter/code/{careCode}"
    rq = requests.get(URL, headers=headers)
    data = rq.json()
    return data['careName']

def get_lost_shelter_by_carecode(careCode):
    load_dotenv()
    headers = {
        'Content-Type': 'application/json',
        'authorization': f"Bearer {os.environ.get('SERVER_TOKEN')}",
    }
    URL = f"http://{os.environ.get('DOMAIN')}:5000/api/lost-shelter/shelter-code/{careCode}"
    rq = requests.get(URL, headers=headers)
    data = rq.json()
    # print('get_lost_shelter_by_carecode')
    # pprint(data)
    return data

def push_sms(phone_shelter_dict):
    load_dotenv()
    client = Client(os.environ.get('TWILIO_ACCOUNT_SID_JM'), os.environ.get('TWILIO_AUTH_TOKEN_JM'))
    for phone_number, shelter_list in phone_shelter_dict.items():
        urls = '\n '.join(set([f"{shelter_dict['shelter_name']} : http://{os.environ.get('DOMAIN')}/api/rescue/care-code/{shelter_dict['shelter_code']}" for shelter_dict in shelter_list]))
        body = f'''
        
        구해줘 댕냥쓰!
        주인님! 
        근처 보호소에서 
        주인을 기다리는 댕냥이들이 새로 왔어요!
        우리 댕냥이가 있는지 확인해주세요!!
        {urls}
        '''
        try:
            message = client.messages.create(
                body=body,
                from_={os.environ.get('TWILIO_PHONENUMBER_JM')},
                to=f"+82{phone_number[1:]}"
                )
        except:
            print("번호를 등록해주시거나 없는 번호입니다.")


def alert_new_notice_sms(result):
    current_count_by_carecode = get_current_count_by_carecode(result)
    target_carecode_list = get_target_shelter(current_count_by_carecode)
    if len(target_carecode_list) == 0:
        print("모든 보호소에서 변동내역이 없습니다.")
        return
    phone_shelter_dict = {}
    for careCode in target_carecode_list:
        lost_shelter_info_list = get_lost_shelter_by_carecode(careCode)
        if len(lost_shelter_info_list) == 0:
            print("해당 보호소는 변동내역이 있지만 알림 받을 사용자가 없습니다.")
            continue           

        for lost_shelter in lost_shelter_info_list:
            phone_number = lost_shelter['phoneNumber'].replace("-","")
            shelter_code = lost_shelter['careCode']
            shelter_name = get_shelter_name_by_carecode(shelter_code)
            phone_shelter_dict.setdefault(phone_number,[])
            phone_shelter_dict[phone_number].append({"shelter_name":shelter_name,"shelter_code":shelter_code})

    print(phone_shelter_dict)
    push_sms(phone_shelter_dict)
    print("sms push complete")
    post_log("sms push complete")

def main():
    load_dotenv()
    db_output = get_db(os.environ.get('DB_NAME')) #"test"
    db_document_count = db_output.rescues.count_documents({})
    print_db_document_count= f'''current DB stored document count : {db_document_count}\n'''
    print(print_db_document_count)
    post_progressbar("====================================================================================="+"<br>")
    post_log(print_db_document_count)
    
    
    API_Key, date = get_requests_params("ApiKey", 1)
    animal_info_totalCount, animal_info_totalPages = get_total_count_pages(API_Key, date)

    # 보호중 데이터가 종료되는 경우 고려해봐야함
    if db_document_count == animal_info_totalCount:
        print_nothing_update = f"we dont have nothing to update! db_document_count: {db_document_count} | animal_info_totalCount : {animal_info_totalCount}\n"
        print(print_nothing_update)
        post_log(print_nothing_update)
        return
    
    db_shelter_info = get_db("test")
    shelter_info_dict = get_shelter_info(db_shelter_info)
    print_pipeline_start = f"{animal_info_totalCount} pipeline start!\n"
    print(print_pipeline_start)
    post_log(print_pipeline_start)
    print_total_page_count = f'''count of total page : {animal_info_totalPages}\n'''
    print(print_total_page_count)
    post_log(print_total_page_count)

    result = [ 
        (
            post_progressbar("|") if idx%10==0 else False,
            lng_lat_dict := get_coord(info_dict['happenPlace'], info_dict['careAddr']),
            {
                "desertionNo": info_dict['desertionNo'],
                "imgUrl": info_dict['popfile'], 
                "happenDate": info_dict['happenDt'], 
                "happenPlace": info_dict['happenPlace'], 
                "kindCode": info_dict['kindCd'], 
                "kindCodeByNum" : 0 if "개" in info_dict['kindCd'] else 1 if "고양이" in info_dict['kindCd'] else 2,
                "colorCode": info_dict['colorCd'], 
                "sexCode": info_dict['sexCd'], 
                "neuteY/N": info_dict['neuterYn'], 
                "noticeStartDate": info_dict['noticeSdt'], 
                "noticeEndDate": info_dict['noticeEdt'], 
                "specialMark": info_dict['specialMark'], 
                "age": info_dict['age'], 
                "weight": info_dict['weight'], 
                "processState": info_dict['processState'], 
                "careCode":  is_good_data(shelter_info_dict, info_dict['careNm']),
                "careAddress": info_dict['careAddr'], 
                "careName": info_dict['careNm'], 
                "careTel": info_dict['careTel'],  
                "officeTel": info_dict['officetel'],
                "happenLatitude" : lng_lat_dict['latitude'],
                "happenLongitude" : lng_lat_dict['longitude'],
                "coords":[lng_lat_dict['longitude'], lng_lat_dict['latitude']]
            }
        )[-1]
        
        for page_number in range(1, animal_info_totalPages+1) 
        for idx, info_dict in enumerate(tqdm(get_info_list_by_page(API_Key, date, page_number)))
    ]

    #alert_new_notice_sms(result)

    db_output.rescues.drop() 
    print_reset_complete = "DB reset complete!\n"
    print(print_reset_complete)
    post_log(print_reset_complete)
    db_output.rescues.insert_many(result)
    print_load_complete = f"{len(result)} pipeline load complete!\n"
    print(print_load_complete)
    post_log(print_load_complete)

start = time.time()
main()
print_total_elapsed_time = f"total elapsed time : {time.time() - start}\n"
print(print_total_elapsed_time)
post_log(print_total_elapsed_time)
post_progressbar("====================================================================================="+"<br>")