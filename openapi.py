import os
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

def get_total_pages(API_Key, date):
    URL = get_url(API_Key, date)
    rq = requests.get(URL)
    data = rq.json()
    animal_info_totalCount = data['response']['body']['totalCount']
    animal_info_totalPages = math.ceil(animal_info_totalCount/1000)
    return animal_info_totalPages

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

def main():
    load_dotenv()

    db_regnotest = get_db("regnotest")
    db_openApi = get_db("openApi")

    API_Key, date = get_requests_params("ApiKey", 3)

    animal_info_totalPages = get_total_pages(API_Key, date)

    shelter_info_dict = get_shelter_info(db_openApi)

    result = [ 
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
            "careCode":  is_good_data(shelter_info_dict,info_dict['careNm']),
            "careAddr": info_dict['careAddr'], 
            "careName": info_dict['careNm'], 
            "careTel": info_dict['careTel'],  
            "officeTel": info_dict['officetel'] 
        }
    for page_number in range(1, animal_info_totalPages+1) 
    for info_dict in get_info_list_by_page(API_Key, date, page_number)
        ]
    db_regnotest.rescues.insert_many(result)


# pprint(result)

# soup = BeautifulSoup(rq.text, "html.parser")
# totalCnt = int(soup.find("totalcount").text)
# print(totalCnt)
# pageCnt = int(totalCnt/1000) + 1
# print(pageCnt)
# for item in soup.find_all("item"):
#     desertionNo = item.find("desertionno").text
#     imgUrl = item.find("popfile").text
#     happenDate = item.find("happendt").text
#     happenPlace = item.find("happenplace").text
#     kindCd = item.find("kindcd").text    
#     colorCd = item.find("colorcd").text
#     sexCode = item.find("sexcd").text
#     neuteYn = item.find("neuteryn").text
#     noticeSdt = item.find("noticesdt").text
#     noticeEdt = item.find("noticeedt").text
#     specialMark = item.find("specialmark").text
#     age = item.find("age").text
#     weight = item.find("weight").text
#     processState = item.find("processstate").text
#     careAddr = item.find("careaddr").text
#     careName = item.find("carenm").text
#     careTel = item.find("caretel").text
#     officeTel = item.find("officetel").text

#     careRegNo = db_openApi.careRegNo.find({"careNm" : careName})
#     careregno = list(careRegNo)
#     try :
#         careCode = careregno[0]['careRegNo']
#     except:
#         careCode = 0
#         print(item)
#         print(careName, careregno)

#     db_regnotest.rescues.insert_one({"desertionNo": desertionNo,"imgUrl": imgUrl, "happenDate": happenDate, "happenPlace": happenPlace, "kindCode": kindCd, "colorCode": colorCd, "sexCode": sexCode, "neuteY/N": neuteYn, "noticeStartDate":noticeSdt, "noticeEndDate": noticeEdt, "specialMark": specialMark, "age": age, "weight": weight, "processState": processState, "careCode": careCode, "careAddr": careAddr, "careName": careName, "careTel": careTel,  "officeTel": officeTel })

# if totalCnt > 1000:
#     while page < pageCnt:
#         page += 1
#         URL = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?bgnde={Date}&endde={endDate}&pageNo={Page}&numOfRows=1000&serviceKey={API}".format(Page=page,Date=InputDate, API=API_Key)

#         rq = requests.get(URL)
#         soup = BeautifulSoup(rq.text, "html.parser")

#         # rescue= []
#         for item in soup.find_all("item"):
#             desertionNo = item.find("desertionno").text
#             imgUrl = item.find("popfile").text
#             happenDate = item.find("happendt").text
#             happenPlace = item.find("happenplace").text
#             kindCd = item.find("kindcd").text    
#             colorCd = item.find("colorcd").text
#             sexCode = item.find("sexcd").text
#             neuteYn = item.find("neuteryn").text
#             noticeSdt = item.find("noticesdt").text
#             noticeEdt = item.find("noticeedt").text
#             specialMark = item.find("specialmark").text
#             age = item.find("age").text
#             weight = item.find("weight").text
#             processState = item.find("processstate").text
#             careAddr = item.find("careaddr").text
#             careName = item.find("carenm").text
#             careTel = item.find("caretel").text
#             officeTel = item.find("officetel").text    
            
#             careRegNo = client.openApi.careRegNo.find({"careNm" : careName})
#             careregno = list(careRegNo)
#             careCode = careregno[0]['careRegNo']

#             db.rescues.insert_one({"desertionNo": desertionNo,"imgUrl": imgUrl, "happenDate": happenDate, "happenPlace": happenPlace, "kindCode": kindCd, "colorCode": colorCd, "sexCode": sexCode, "neuteY/N": neuteYn, "noticeStartDate":noticeSdt, "noticeEndDate": noticeEdt, "specialMark": specialMark, "age": age, "weight": weight, "processState": processState, "careCode": careCode, "careAddr": careAddr, "careName": careName, "careTel": careTel,  "officeTel": officeTel })