import requests
from bs4 import BeautifulSoup
# import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongodb_URL = os.environ.get('mongodbURL')
client = MongoClient(mongodb_URL)
db = client.test

API_Key = os.environ.get("ApiKey")
InputDate = int(input("Date : "  ))

page = 1
URL = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?bgnde={Date}&pageNo={Page}&numOfRows=1000&serviceKey={API}".format(Page=page,Date=InputDate, API=API_Key)

rq = requests.get(URL)
soup = BeautifulSoup(rq.text, "html.parser")

totalCnt = int(soup.find("totalcount").text)
print(totalCnt)
pageCnt = int(totalCnt/1000) + 1
print(pageCnt)
# rescue = []
for item in soup.find_all("item"):
    desertionNo = item.find("desertionno").text
    imgUrl = item.find("filename").text
    happenDate = item.find("happendt").text
    happenPlace = item.find("happenplace").text
    kindCd = item.find("kindcd").text    
    colorCd = item.find("colorcd").text
    sexCode = item.find("sexcd").text
    neuteYn = item.find("neuteryn").text
    noticeSdt = item.find("noticesdt").text
    noticeEdt = item.find("noticeedt").text
    specialMark = item.find("specialmark").text
    age = item.find("age").text
    weight = item.find("weight").text
    processState = item.find("processstate").text
    careAddr = item.find("careaddr").text
    careName = item.find("carenm").text
    careTel = item.find("caretel").text
    officeTel = item.find("officetel").text
    # rescue.append([kindCd, happenDt, noticeSdt, noticeEdt, processState, findplace, careAddr])
    db.rescues.insert_one({"desertionNo": desertionNo,"imgUrl": imgUrl, "happenDate": happenDate, "happenPlace": happenPlace, "kindCode": kindCd, "colorCode": colorCd, "sexCode": sexCode, "neuteY/N": neuteYn, "noticeStartDate":noticeSdt, "noticeEndDate": noticeEdt, "specialMark": specialMark, "age": age, "weight": weight, "processState": processState, "officeTel": officeTel })

# rescue_df = pd.DataFrame(rescue, columns=["KindCode","HappenDate", "NoticeSDate", "NoticeEdate", "State", "findplace", "Shelter"])

# rescue_df.to_csv('openApi.csv', encoding='utf-8') 

if totalCnt > 1000:
    while page < pageCnt:
        page += 1
        URL = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?bgnde={Date}&endde={endDate}&pageNo={Page}&numOfRows=1000&serviceKey={API}".format(Page=page,Date=InputDate,endDate = EndDate, API=API_Key)

        rq = requests.get(URL)
        soup = BeautifulSoup(rq.text, "html.parser")

        # rescue= []
        for item in soup.find_all("item"):
            desertionNo = item.find("desertionno").text
            imgUrl = item.find("filename").text
            happenDate = item.find("happendt").text
            happenPlace = item.find("happenplace").text
            kindCd = item.find("kindcd").text    
            colorCd = item.find("colorcd").text
            sexCode = item.find("sexcd").text
            neuteYn = item.find("neuteryn").text
            noticeSdt = item.find("noticesdt").text
            noticeEdt = item.find("noticeedt").text
            specialMark = item.find("specialmark").text
            age = item.find("age").text
            weight = item.find("weight").text
            processState = item.find("processstate").text
            careAddr = item.find("careaddr").text
            careName = item.find("carenm").text
            careTel = item.find("caretel").text
            officeTel = item.find("officetel").text
            # rescue.append([kindCd, happenDt, noticeSdt, noticeEdt, processState, findplace, careAddr])
            
            db.rescues.insert_one({"desertionNo": desertionNo,"imgUrl": imgUrl, "happenDate": happenDate, "happenPlace": happenPlace, "kindCode": kindCd, "colorCode": colorCd, "sexCode": sexCode, "neuteY/N": neuteYn, "noticeStartDate":noticeSdt, "noticeEndDate": noticeEdt, "specialMark": specialMark, "age": age, "weight": weight, "processState": processState, "officeTel": officeTel })

        # rescue_df = pd.DataFrame(rescue, columns=["KindCode","HappenDate", "NoticeSDate", "NoticeEdate", "State", "findplace", "Shelter"])

        # rescue_df.to_csv('openApi.csv', mode='a', encoding='utf-8', header=False)