import os
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()


    
def address2coord(address, careregno):
    preprocess_address = address.split("(")[0]
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"KakaoAK {os.environ.get('KAKAO_REST_API_KEY')}",
        'Host': 'dapi.kakao.com',
    }
    URL = f"https://dapi.kakao.com/v2/local/search/address.json?query={preprocess_address}"

    try:
        rq = requests.get(URL, headers=headers)
        data = rq.json()

        if len(data['documents'])==0:
            print(careregno)
            pprint(data)
            print(address)
            print()
            return
            
        lng = float(data['documents'][0]['address']['x']) # 경도 127.XX
        lat = float(data['documents'][0]['address']['y']) # 위도 36.xx

    except requests.exceptions.Timeout as errd:
        # pprint(data)
        # print(address)
        print("Timeout Error : ", errd)
        
    except requests.exceptions.ConnectionError as errc:
        # pprint(data)
        # print(address)
        print("Error Connecting : ", errc)
        
    except requests.exceptions.HTTPError as errb:
        # pprint(data)
        # print(address)
        print("Http Error : ", errb)

    except requests.exceptions.RequestException as erra:
        # pprint(data)
        # print(address)
        print("AnyException : ", erra)
        print()


    
    return lng, lat

def address2coord_test(address):
    test_addr = address2coord(address)
    pprint(test_addr)

# address2coord_test("대전광역시 대덕구 한밭대로1114번길 34")

mongodb_URL = os.environ.get('mongodbURL')
client = MongoClient(mongodb_URL)
db0 = client.openApi
db1 = client.test

API_Key = os.environ.get("ApiKey")

shelters = []
for x in db0.careRegNo.find():
    shelters.append(x)

CAN_NOT_ADDRESS = list()
# CAN_NOT_ADDRESS_ADDR = []
# CAN_NOT_ADDRESS_NAME = []
for x in shelters:
    careregno = x['careRegNo']

    URL = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?care_reg_no={careregno}&numOfRows=1&serviceKey={API}".format(careregno=careregno, API=API_Key)

    rq = requests.get(URL)
    soup = BeautifulSoup(rq.text, "html.parser")

    for item in soup.find_all("item"):
        careAddr = item.find("careaddr").text
        careName = item.find("carenm").text
        careTel = item.find("caretel").text
        if careregno == "327343201500001":
            careAddr = "대구 북구 호국로 229"
        if careregno == "344462200900001":
            careAddr = "충남 태안군 태안읍 중앙로 31-2"
        if careregno == "345464201100004":
            careAddr = "전북 전주시 완산구 기린대로 139"
        if careregno == "346499201300001":
            careAddr = "전라남도 완도군 신지면 송곡리 636-1"
        if careregno == "348541201300001":
            careAddr = "경상남도 창녕군 고암면 억만리 28"
        if careregno == "348528201000001":
            careAddr = "경남 창원시 마산합포구 진북면 지산2길 139-112"
        if careregno == "311322200900001":
            careAddr = "경기도 양주시 남면 감악산로 63-37"
       
        #      or careregno == "344462200900001" :
        #     print('items')
        #     print(item)
        #     continue
        #     print('aaaa')
        try:
            lng, lat = address2coord(careAddr, careregno)
        except:
            CAN_NOT_ADDRESS.append({"careregno":careregno,"careName":careName, "careAddr":careAddr})
            print(careregno, careAddr)

        db1.shelters.insert_one({"careCode": careregno, "careAddress": careAddr, "careName": careName, "careTel": careTel, "longitude": lng, "latitude": lat})

print(CAN_NOT_ADDRESS)