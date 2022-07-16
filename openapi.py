import os
import time
import math
import requests
from datetime import datetime, timedelta
from pymongo import MongoClient
from dotenv import load_dotenv
from pprint import pprint

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
    date = (datetime.today()- timedelta(days_ago)).strftime("%Y%m%d")
    return API_Key, date

def get_total_count_pages(API_Key, date):
    URL = get_url(API_Key, date)
    rq = requests.get(URL)
    data = rq.json()
    animal_info_totalCount = data['response']['body']['totalCount']
    animal_info_totalPages = math.ceil(animal_info_totalCount/1000)
    return animal_info_totalCount, animal_info_totalPages

def get_info_list_by_page(API_Key, date, page_number):
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
        print(key)
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

    if len(data['documents'])==0:
        pprint(data)
        print(address)
        print("address2coord Error")
        return
        
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
    if ('documents' not in data) or (len(data['documents']==0)):
        return 0
    return data

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
    print(result)
    return result

def get_coord(place, shelter_address):
    data = place2coord(place)
    if data == 0:
        data = place2coord(preprocessing_data(place))
        if data == 0:
            return address2coord(shelter_address)
    return get_center_coord(data)

def main():
    load_dotenv()
    db_output = get_db("regnotest")
    db_document_count = db_output.rescues.count_documents({})
    print(db_document_count)
    
    API_Key, date = get_requests_params("ApiKey", 11)
    animal_info_totalCount, animal_info_totalPages = get_total_count_pages(API_Key, date)

    # 보호중 데이터가 종료되는 경우 고려해봐야함
    if db_document_count == animal_info_totalCount:
        print("업데이트할 항목이 없습니다!")
        print(f"db_document_count: {db_document_count} | animal_info_totalCount : {animal_info_totalCount}")
        return
    
    db_shelter_info = get_db("test")
    shelter_info_dict = get_shelter_info(db_shelter_info)
    print(f"{animal_info_totalCount}건 파이프라인 가동!")
    result = [ 
        (
            lng_lat_dict := get_coord(info_dict['happenPlace'], info_dict['careAddr']),
            {
                "desertionNo": info_dict['desertionNo'],
                "imgUrl": info_dict['popfile'], 
                "happenDate": info_dict['happenDt'], 
                "happenPlace": info_dict['happenPlace'], 
                "kindCode": info_dict['kindCd'], 
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
                "careAddr": info_dict['careAddr'], 
                "careName": info_dict['careNm'], 
                "careTel": info_dict['careTel'],  
                "officeTel": info_dict['officetel'],
                "latitude" : lng_lat_dict['latitude'],
                "longitude" : lng_lat_dict['longitude']
            }
        )[1]
        
        for page_number in range(1, animal_info_totalPages+1) 
        for info_dict in get_info_list_by_page(API_Key, date, page_number)
    ]
    db_output.rescues.drop() 
    print("초기화 완료!")
    db_output.rescues.insert_many(result)
    print(f"{len(result)}건 파이프라인 로드 완료!")

start = time.time()
main()
print("time :", time.time() - start)