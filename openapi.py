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

def get_url(API_Key, ten_days_ago, page_number = 1):
    URL = f"http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?bgnde={ten_days_ago}&numOfRows=1000&pageNo={page_number}&serviceKey={API_Key}&_type=json"
    return URL

def get_requests_params():
    API_Key = os.environ.get("ApiKey")
    ten_days_ago = (datetime.today()- timedelta(10)).strftime("%Y%m%d")
    return API_Key, ten_days_ago

load_dotenv()

db_regnotest = get_db("regnotest")
db_openApi = get_db("openApi")

API_Key, ten_days_ago = get_requests_params()


URL = get_url(API_Key, ten_days_ago)
rq = requests.get(URL)
data = rq.json()

animal_info_list = data['response']['body']['items']['item']
animal_info_totalCount = data['response']['body']['totalCount']
animal_info_totalPages = math.ceil(animal_info_totalCount/1000)




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