import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongodb_URL = os.environ.get('mongodbURL')
client = MongoClient(mongodb_URL)
db = getattr(client, os.environ.get('DB_NAME')) #"test"

API_Key = os.environ.get("ApiKey")

kind = [417000, 422400, 429900]
URL = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/kind?up_kind_cd={kind}&serviceKey={API}".format(kind=kind[0], API=API_Key)

rq = requests.get(URL)
soup = BeautifulSoup(rq.text, "html.parser")

for item in soup.find_all("item"):
    kindCd = item.find("kindcd").text
    kindNm = item.find("knm").text

    db.kindCd.insert_one({"upKindCd": "개","kindCd": kindCd, "kindNm": kindNm })

URL = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/kind?up_kind_cd={kind}&serviceKey={API}".format(kind=kind[1], API=API_Key)

rq = requests.get(URL)
soup = BeautifulSoup(rq.text, "html.parser")

for item in soup.find_all("item"):
    kindCd = item.find("kindcd").text
    kindNm = item.find("knm").text

    db.kindCd.insert_one({"upKindCd": "고양이","kindCd": kindCd, "kindNm": kindNm })

URL = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/kind?up_kind_cd={kind}&serviceKey={API}".format(kind=kind[2], API=API_Key)

rq = requests.get(URL)
soup = BeautifulSoup(rq.text, "html.parser")

for item in soup.find_all("item"):
    kindCd = item.find("kindcd").text
    kindNm = item.find("knm").text

    db.kindCd.insert_one({"upKindCd": "기타","kindCd": kindCd, "kindNm": kindNm })