import requests
from bs4 import BeautifulSoup
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongodb_URL = os.environ.get('mongodbURL')
client = MongoClient(mongodb_URL)
db = client.openApi

API_Key = os.environ.get("ApiKey")
InputDate = int(input("Date : "  ))
EndDate = InputDate + 10
page = 1
URL = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?bgnde={Date}&endde={endDate}&pageNo={Page}&numOfRows=1000&serviceKey={API}".format(Page=page,Date=InputDate,endDate = EndDate, API=API_Key)

rq = requests.get(URL)
soup = BeautifulSoup(rq.text, "html.parser")

rescue= []
totalCnt = int(soup.find("totalcount").text)
print(totalCnt)
pageCnt = int(totalCnt/1000) + 1
print(pageCnt)
# rescue = []
for item in soup.find_all("item"):
    kindCd = item.find("kindcd").text
    happenDt = item.find("happendt").text
    noticeSdt = item.find("noticesdt").text
    noticeEdt = item.find("noticeedt").text
    processState = item.find("processstate").text
    findplace = item.find("happenplace").text
    careAddr = item.find("careaddr").text
    # rescue.append([kindCd, happenDt, noticeSdt, noticeEdt, processState, findplace, careAddr])
    db.test.insert_one({"kindCd": kindCd, "happenDt": happenDt, "noticeSdt" : noticeSdt, "noticeEdt":noticeEdt,"processState": processState, "findplace":findplace, "careAddr":careAddr})

# rescue_df = pd.DataFrame(rescue, columns=["KindCode","HappenDate", "NoticeSDate", "NoticeEdate", "State", "findplace", "Shelter"])

# rescue_df.to_csv('openApi.csv', encoding='utf-8') 

if totalCnt > 1000:
    while page < pageCnt:
        page += 1
        URL = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?bgnde={Date}&endde={endDate}&pageNo={Page}&numOfRows=1000&serviceKey={API}".format(Page=page,Date=InputDate,endDate = EndDate, API=API_Key)

        rq = requests.get(URL)
        soup = BeautifulSoup(rq.text, "html.parser")

        rescue= []
        for item in soup.find_all("item"):
            kindCd = item.find("kindcd").text
            happenDt = item.find("happendt").text
            noticeSdt = item.find("noticesdt").text
            noticeEdt = item.find("noticeedt").text
            processState = item.find("processstate").text
            findplace = item.find("happenplace").text
            careAddr = item.find("careaddr").text
            # rescue.append([kindCd, happenDt, noticeSdt, noticeEdt, processState, findplace, careAddr])
            db.test.insert_one({"kindCd": kindCd, "happenDt": happenDt, "noticeSdt" : noticeSdt, "noticeEdt":noticeEdt,"processState": processState, "findplace":findplace, "careAddr":careAddr});

        # rescue_df = pd.DataFrame(rescue, columns=["KindCode","HappenDate", "NoticeSDate", "NoticeEdate", "State", "findplace", "Shelter"])

        # rescue_df.to_csv('openApi.csv', mode='a', encoding='utf-8', header=False)