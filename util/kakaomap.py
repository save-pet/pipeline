import os
import requests

def address2coord(address):
    preprocess_address = address.split("(")[0]
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"KakaoAK {os.environ.get('KAKAO_REST_API_KEY')}",
        'Host': 'dapi.kakao.com',
    }
    URL = f"https://dapi.kakao.com/v2/local/search/address.json?query={preprocess_address}"

    rq = requests.get(URL, headers=headers)
    data = rq.json()

    if ('documents' not in data) or (len(data['documents'])==0):
        # pprint(data)
        # print(address)
        # print("address2coord Error")
        return 0
        
    lng = float(data['documents'][0]['address']['x']) # 경도 127.XX
    lat = float(data['documents'][0]['address']['y']) # 위도 36.xx
    return {"latitude": lat, "longitude": lng}

def place2coord(place):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"KakaoAK {os.environ.get('KAKAO_REST_API_KEY')}",
        'Host': 'dapi.kakao.com',
    }
    URL = f"https://dapi.kakao.com/v2/local/search/keyword.json?query={place}"

    rq = requests.get(URL, headers=headers)
    data = rq.json()
    if ('documents' not in data) or (len(data['documents'])==0):
        return 0
    return data['documents']

def preprocessing_data(place):
    address = place.split()
    preprocess_data = [elem for elem in address if '동' in elem or '리' in elem or '면' in elem or '읍' in elem or '시' in elem]
    if len(preprocess_data)==0:
        return 0
    return preprocess_data[-1]

def get_center_coord(data):
    cunsum_dict = {"lat": 0, "lng": 0}
    for elem in data:
        cunsum_dict['lat'] += float(elem['y'])
        cunsum_dict['lng'] += float(elem['x'])
    result = {"latitude": float(cunsum_dict['lat'])/len(data), "longitude": float(cunsum_dict['lng'])/len(data)}
    # print(result)
    return result

def get_coord(place, shelter_address):
    data = place2coord(place)
    if data == 0:
        data = place2coord(preprocessing_data(place))
        if data == 0:
            coord = address2coord(shelter_address)
            if coord == 0:
                return {"latitude": 37.23988837533657, "longitude": 131.8719452704162}
            else:
                return coord
        else: 
            return get_center_coord(data)
    else: 
        return get_center_coord(data)
