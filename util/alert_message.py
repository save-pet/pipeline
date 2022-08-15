import os
import requests
from datetime import datetime, timedelta
from twilio.rest import Client
from dotenv import load_dotenv
from pytz import timezone

def post_log(log):
    try:
        with open('/var/www/html/index.html', 'a', encoding="utf-8") as html_file:
            time = datetime.now(timezone('Asia/Seoul')).strftime('[%Y%m%d %H:%M:%S] ')
            html_file.write(time + log + "<br>")
    except:
        pass

def post_progressbar(bar):
    try:
        with open('/var/www/html/index.html', 'a', encoding="utf-8") as html_file:
            html_file.write(bar)
    except:
        pass

def get_current_count_by_carecode(result):
    count_dict = {}
    for result_dict in result:
        care_code = result_dict['careCode']
        count_dict[care_code] = count_dict.setdefault(care_code, 0) + 1
    return count_dict

def get_previous_count_by_carecode(care_code):
    load_dotenv()
    headers = {
        'Content-Type': 'application/json',
        'authorization': f"Bearer {os.environ.get('SERVER_TOKEN')}",
    }
    URL = f"http://{os.environ.get('DOMAIN')}:5000/api/rescue/care-code/count/{care_code}"
    rq = requests.get(URL, headers=headers)
    data = rq.json()
    return data

def get_target_shelter(current_count_by_carecode):
    target_shelter = []
    for care_code, currrent_count in current_count_by_carecode.items():
        previous_count = get_previous_count_by_carecode(care_code)
        # print("previous_count")
        # print(previous_count)
        if currrent_count != previous_count:
            target_shelter.append(care_code)
    return target_shelter

def get_shelter_name_by_carecode(careCode):
    load_dotenv()
    headers = {
        'Content-Type': 'application/json',
        'authorization': f"Bearer {os.environ.get('SERVER_TOKEN')}",
    }
    URL = f"http://{os.environ.get('DOMAIN')}:5000/api/shelter/code/{careCode}"
    rq = requests.get(URL, headers=headers)
    data = rq.json()
    return data['careName']

def get_lost_shelter_by_carecode(careCode):
    load_dotenv()
    headers = {
        'Content-Type': 'application/json',
        'authorization': f"Bearer {os.environ.get('SERVER_TOKEN')}",
    }
    URL = f"http://{os.environ.get('DOMAIN')}:5000/api/lost-shelter/shelter-code/{careCode}"
    rq = requests.get(URL, headers=headers)
    data = rq.json()
    # print('get_lost_shelter_by_carecode')
    # pprint(data)
    return data

def push_sms(phone_shelter_dict):
    load_dotenv()
    client = Client(os.environ.get('TWILIO_ACCOUNT_SID_JM'), os.environ.get('TWILIO_AUTH_TOKEN_JM'))
    for phone_number, shelter_list in phone_shelter_dict.items():
        urls = '\n '.join(set([f"{shelter_dict['shelter_name']} : http://{os.environ.get('DOMAIN')}/api/rescue/care-code/{shelter_dict['shelter_code']}" for shelter_dict in shelter_list]))
        body = f'''
        
        구해줘 댕냥쓰!
        주인님! 
        근처 보호소에서 
        주인을 기다리는 댕냥이들이 새로 왔어요!
        우리 댕냥이가 있는지 확인해주세요!!
        {urls}
        '''
        try:
            message = client.messages.create(
                body=body,
                from_={os.environ.get('TWILIO_PHONENUMBER_JM')},
                to=f"+82{phone_number[1:]}"
                )
        except:
            print("번호를 등록해주시거나 없는 번호입니다.")


def alert_new_notice_sms(result):
    current_count_by_carecode = get_current_count_by_carecode(result)
    target_carecode_list = get_target_shelter(current_count_by_carecode)
    if len(target_carecode_list) == 0:
        print("모든 보호소에서 변동내역이 없습니다.")
        return
    phone_shelter_dict = {}
    for careCode in target_carecode_list:
        lost_shelter_info_list = get_lost_shelter_by_carecode(careCode)
        if len(lost_shelter_info_list) == 0:
            print("해당 보호소는 변동내역이 있지만 알림 받을 사용자가 없습니다.")
            continue           

        for lost_shelter in lost_shelter_info_list:
            phone_number = lost_shelter['phoneNumber'].replace("-","")
            shelter_code = lost_shelter['careCode']
            shelter_name = get_shelter_name_by_carecode(shelter_code)
            phone_shelter_dict.setdefault(phone_number,[])
            phone_shelter_dict[phone_number].append({"shelter_name":shelter_name,"shelter_code":shelter_code})

    print(phone_shelter_dict)
    push_sms(phone_shelter_dict)
    print("sms push complete")
    post_log("sms push complete")