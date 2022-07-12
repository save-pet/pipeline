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

shelters = []
for x in db.careRegNo.find():
    shelters.append(x)

for x in shelters:
    careregno = x['careRegNo']

    URL = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?care_reg_no={careregno}&numOfRows=1&serviceKey={API}".format(careregno=careregno, API=API_Key)

    rq = requests.get(URL)
    soup = BeautifulSoup(rq.text, "html.parser")

    for item in soup.find_all("item"):
        careAddr = item.find("careaddr").text
        careName = item.find("carenm").text
        careTel = item.find("caretel").text

        db.shelters.insert_one({"careCode": careregno, "careAddr": careAddr, "careName": careName, "careTel": careTel })
