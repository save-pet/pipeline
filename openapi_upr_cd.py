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

orgCd = []
for x in db.orgCd.find():
    orgCd.append(x)

for x in orgCd:
    uprCd = x['orgCd']

    URL = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/sigungu?upr_cd={orgCd}&serviceKey={API}".format(orgCd=uprCd, API=API_Key)
    rq = requests.get(URL)
    soup = BeautifulSoup(rq.text, "html.parser")

    for item in soup.find_all("item"):
        orgCd = item.find("orgcd").text
        orgdownNm = item.find("orgdownnm").text

        db.uprCd.insert_one({"uprCd": uprCd, "orgCd": orgCd, "orgdownNm": orgdownNm })
