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

totalCd = []
for x in db.uprCd.find():
    totalCd.append(x)

for x in totalCd:
    uprcd = x['uprCd']
    orgcd = x['orgCd']
    URL = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/shelter?upr_cd={uprCd}&org_cd={orgCd}&serviceKey={API}".format(uprCd=uprcd, orgCd=orgcd, API=API_Key)

    rq = requests.get(URL)
    soup = BeautifulSoup(rq.text, "html.parser")
    
    for item in soup.find_all("item"):
        careRegNo = item.find("careregno").text
        careNm = item.find("carenm").text

        db.careRegNo.insert_one({"careRegNo":careRegNo, "careNm":careNm })
