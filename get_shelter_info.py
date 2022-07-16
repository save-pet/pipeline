import os
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
API_Key = os.environ.get("ApiKey")


def address2coord(address):
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
            pprint(data)
            print(address)
            print()
            return
            
        lng = float(data['documents'][0]['address']['x']) # 경도 127.XX
        lat = float(data['documents'][0]['address']['y']) # 위도 36.xx

    except requests.exceptions.Timeout as errd:
        pprint(data)
        print(address)
        print("Timeout Error : ", errd)
        
    except requests.exceptions.ConnectionError as errc:
        pprint(data)
        print(address)
        print("Error Connecting : ", errc)
        
    except requests.exceptions.HTTPError as errb:
        pprint(data)
        print(address)
        print("Http Error : ", errb)

    except requests.exceptions.RequestException as erra:
        pprint(data)
        print(address)
        print("AnyException : ", erra)
        print()


    
    return lng, lat

def get_shelter_detail_info(care_reg_no):
    try:
        URL = f"http://apis.data.go.kr/1543061/animalShelterSrvc/shelterInfo?care_reg_no={care_reg_no}&serviceKey={API_Key}&_type=json"

        rq = requests.get(URL)
        data = rq.json()

        return data

    except requests.exceptions.Timeout as errd:
        print("Timeout Error : ", errd)
        
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting : ", errc)
        
    except requests.exceptions.HTTPError as errb:
        print("Http Error : ", errb)

    except requests.exceptions.RequestException as erra:
        print("AnyException : ", erra)


    


mongodb_URL = os.environ.get('mongodbURL')
client = MongoClient(mongodb_URL)
db = client.openApi
# region_code_dicts = db.uprCd.find()
shelter_info_dicts = db.careRegNo.find()

def get_shelter_code(upr_cd, org_cd):
    try:
        URL = f"http://apis.data.go.kr/1543061/abandonmentPublicSrvc/shelter?upr_cd={upr_cd}&org_cd={org_cd}&serviceKey={API_Key}&_type=json"

        rq = requests.get(URL)
        data = rq.json()
        return data

    except requests.exceptions.Timeout as errd:
        print("Timeout Error : ", errd)
        
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting : ", errc)
        
    except requests.exceptions.HTTPError as errb:
        print("Http Error : ", errb)

    except requests.exceptions.RequestException as erra:
        print("AnyException : ", erra)

# def extract_data(dict_data):
#     return dict_data['response']['body']['items']['item'][0]

result_list = list()

# for elem in region_code_dicts:
#     shelter_info_response = get_shelter_code(elem['uprCd'],elem['orgCd'])
#     if 'item' not in shelter_info_response['response']['body']['items']:
#         print("get_shelter_code_ERROR")
#         print(elem['orgdownNm'])
#         pprint(shelter_info_response)
#         continue
#     shelter_info_dicts = shelter_info_response['response']['body']['items']['item']

for shelter_info_dict in shelter_info_dicts:
    # print(shelter_info_dict)

    shelter_detail_info_response = get_shelter_detail_info(shelter_info_dict['careRegNo'])
    try:
        if len(shelter_detail_info_response['response']['body']['items']) == 0:
            print("get_shelter_detail_info_ERROR")
            print(shelter_info_dict['careRegNo'])
            print(shelter_detail_info_response)
            continue
    except:
        pprint(shelter_detail_info_response)

    shelter_detail_info_dict = get_shelter_detail_info(shelter_info_dict['careRegNo'])['response']['body']['items']['item'][0]
    if 'careAddr' not in shelter_info_dict:
        continue
    if 'lng' not in shelter_info_dict:
        # print()
        # print("NAME ERROR")
        # pprint(shelter_detail_info_dict)
        # pprint(shelter_info_dict)
        lng, lat = address2coord(shelter_detail_info_dict['careAddr'].split("(")[0])
        shelter_detail_info_dict['lng'] = lng
        shelter_detail_info_dict['lat'] = lat

    result_dict = {
        "careCode": shelter_info_dict['careRegNo'], 
        "careAddr": shelter_detail_info_dict['careAddr'], 
        "careName": shelter_info_dict ['careNm'], 
        "careTel": shelter_detail_info_dict['careTel'],
        "lng": shelter_detail_info_dict['lng'], 
        "lat": shelter_detail_info_dict['lat']
    }

    result_list.append(result_dict)


pprint(result_list[:10])

# shelter_detail_info_dict = get_shelter_detail_info('350650201200001')['response']['body']['items']['item'][0]

# shelter_info_dict['lat'] = shelter_detail_info_dict['lat']
# shelter_info_dict['lng'] = shelter_detail_info_dict['lng']


# pprint(shelter_info_dict)
# db.shelters.insert_one({