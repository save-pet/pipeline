import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongodb_URL = os.environ.get('mongodbURL')
client = MongoClient(mongodb_URL)
db = client.openApi

API_Key = os.environ.get("ApiKey")

page = 1
URL = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/sido?numOfRows=1000&pageNo={Page}&serviceKey={API}".format(Page=page, API=API_Key)

rq = requests.get(URL)
soup = BeautifulSoup(rq.text, "html.parser")

totalCnt = int(soup.find("totalcount").text)
print(totalCnt)
pageCnt = int(totalCnt/1000) + 1
print(pageCnt)

for item in soup.find_all("item"):
    orgCd = item.find("orgcd").text
    orgdownNm = item.find("orgdownnm").text

    db.orgCd.insert_one({"orgCd": orgCd, "orgdownNm": orgdownNm })


if totalCnt > 1000:
    while page < pageCnt:
        page += 1
        URL = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/sido?numOfRows=1000&pageNo={Page}&serviceKey={API}".format(Page=page, API=API_Key)

        rq = requests.get(URL)
        soup = BeautifulSoup(rq.text, "html.parser")

        for item in soup.find_all("item"):
            orgCd = item.find("orgcd").text
            orgdownNm = item.find("orgdownnm").text

            db.orgCd.insert_one({"orgCd": orgCd, "orgdownNm": orgdownNm })