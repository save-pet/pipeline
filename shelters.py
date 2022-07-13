import os
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()


def address2coord(address):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"KakaoAK {os.environ.get('KAKAO_REST_API_KEY')}",
        'Host': 'dapi.kakao.com',
    }
    URL = f"https://dapi.kakao.com/v2/local/search/address.json?query={address}"
    response = requests.get(URL, headers=headers)
    data = response.json()

    lng = float(data['documents'][0]['address']['x']) # 경도 127.XX
    lat = float(data['documents'][0]['address']['y']) # 위도 36.xx
    
    return lng, lat

def address2coord_test(address):
    test_addr = address2coord(address)
    pprint(test_addr)

# address2coord_test("대전광역시 대덕구 한밭대로1114번길 34")

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
        lng, lat = address2coord(careAddr)

        db.shelters.insert_one({"careCode": careregno, "careAddr": careAddr, "careName": careName, "careTel": careTel, "lng": lng, "lat": lat})


