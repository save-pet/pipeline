# openApi_rescue

openapi_upr_cd.py -> 시도 코드 불러오기

openapi_org_cd.py -> 시군구 코드 불러오기

openapi_kind.py -> 품종 코드 불러오기

openapi_care_reg_no.py -> 보호소 코드 불러오기

openapi.py -> 보호 동물 불러오기

shelter.py -> 보호소 정보 불러오기

<br />

# 구해줘 댕냥스 🐶🐱

> 잃어버린 우리 댕냥이<br />
> 하루종일 보호소 공고 확인하셨다구요?<br />
> 보호소에서 찾는건 <b>구해줘 댕냥스</b>에게 맡겨주세요!🍳<br />
> 잃어버린 위치 주변에서 찾은 댕냥이들을 알려줄게요🦾 <br />

<br/>

> ## 어떤 서비스인가요?

- 유기동물보호소에 새로운 구조 여부 알림 서비스 ( 반려동물을 잃어버린 위치의 주변에 있는 보호소에서 새로운 구조가 있다면 주인에게 알림을 보내드립니다. )

<br/>

> ## 누구를 위한 서비스인가요?

- <b>반려동물을 잃어버린 주인</b>이 사용자 입니다.

<br/>

> ## 해결하려는 문제가 무엇이고 어떻게 해결하였나요?

1. 반려동물을 잃어버린 사람이 실시간으로 보호소 구조 공고를 확인하는 번거로움 <br/>(입소 후 10일이 지나면 안락사를 진행합니다.) <br/>
   -> <b>SMS 알림 서비스</b>

2. 거주 지역 보호소만 확인하느라 다른 지역 주변 보호소 구조 공고를 놓치는 경우 <br/>(중형견 같은 경우 하루 만에 옆 도시로 넘어갈 수 있습니다.) <br/>
   -> <b>위치 기반</b> (반경 N km 내 보호소 새롭게 구조된 내역 알림)

<br/>

> ## 문제를 해결한다면 무엇이 더 나아질까요?

- 안타깝게 안락사 당하는 반려동물을 줄일 수 있습니다.
- 주인이 반려동물 찾기 위한 다른 일에 집중할 수 있습니다.
- 분실 데이터가 많이 올라온다면 추후 맹견 알림 서비스를 하여 개물림 사고를 예방할 수 있습니다.

<br/>

> ## 기존에는 이런 서비스가 없었나요?

- 비슷한 서비스로 포인핸드가 있습니다. 포인핸드는 단순히 사용자가 선택한 관할지역 기준 보호소 구조 공고만 제공합니다.
- 우리 서비스에서는 반경 Nkm 위치 기반으로 관할지역과 상관없고 알림까지 받을 수 있습니다.

<br/>

> ## 기능을 간단히 정리해주세요.

- 주제 : 반려동물을 잃어버린 위치 주변의 유기동물보호소에서 새롭게 구조된 동물 여부를 문자로 주인에게 알려주는 서비스
- 메인기능 :
  - 실종 장소 주변 보호소에서 새롭게 구조된 동물 여부 <b>알림 기능</b>
  - 보호소에서 구조한 위치와 정보를 나타내는 <b>보호소 구조 공고 지도 기능</b>
  - 실종 위치와 번호를 등록하는 <b>실종 등록 기능</b>
- 서브기능 :
  - 로그인/회원가입
  - 보호소 구조 공고 목록
  - 분실 목록
  - 마이페이지
  - 관리자 페이지
  - 애매.. 위에 와이어프레임 스토리보드 및 유저 시나리오 있어야 할듯

<br/>

> ## 실행방법

```bash
@~project-templet> npm install --global yarn
@~project-templet> npm install
@~project-templet> yarn setup
@~project-templet> yarn start

```

## Stack

### FRONT

<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/> <img src="https://img.shields.io/badge/Tailwind CSS-06B6D4?style=flat-square&logo=Tailwind CSS&logoColor=white"/> <img src="https://img.shields.io/badge/Font Awesome-528DD7?style=flat-square&logo=Font Awesome&logoColor=white"/> <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=React&logoColor=white"/> <img src="https://img.shields.io/badge/Nodemon-76D04B?style=flat-square&logo=Nodemon&logoColor=white"/> <img src="https://img.shields.io/badge/Kakao Map API-FFCD00?style=flat-square&logo=Kakao&logoColor=white"/> <img src="https://img.shields.io/badge/React Kakao Maps SDK-FFCD00?style=flat-square&logo=Kakao&logoColor=white"/>

### BACK

<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/> <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=Node.js&logoColor=white"/> <img src="https://img.shields.io/badge/Yarn-2C8EBB?style=flat-square&logo=Yarn&logoColor=white"/> <img src="https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white"/> <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=MongoDB&logoColor=white"/> <img src="https://img.shields.io/badge/NGINX-009639?style=flat-square&logo=NGINX&logoColor=white"/> <img src="https://img.shields.io/badge/PM2-2B037A?style=flat-square&logo=PM2&logoColor=white"/>

### DATA

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Google Cloud Compute Engine-4285F4?style=flat-square&logo=Google Cloud&logoColor=white"/> <img src="https://img.shields.io/badge/Linux Crontab-FCC624?style=flat-square&logo=Linux&logoColor=white"/> <img src="https://img.shields.io/badge/Twilio SMS-F22F46?style=flat-square&logo=Twilio&logoColor=white"/> <img src="https://img.shields.io/badge/PyMongo-47A248?style=flat-square&logo=MongoDB&logoColor=white"/> <img src="https://img.shields.io/badge/Apache-D22128?style=flat-square&logo=Apache&logoColor=white"/> <img src="https://img.shields.io/badge/Shell Script-FFD500?style=flat-square&logo=Shell&logoColor=white"/> <img src="https://img.shields.io/badge/공공데이터API-336699?style=flat-square&logo=Publons&logoColor=white"/>

### Collabo

<img src="https://img.shields.io/badge/GitMoji-F05032?style=flat-square&logo=Git&logoColor=white"/> <img src="https://img.shields.io/badge/ESLint-4B32C3?style=flat-square&logo=ESLint&logoColor=white"/> <img src="https://img.shields.io/badge/Prettier-F7B93E?style=flat-square&logo=Prettier&logoColor=white"/> <img src="https://img.shields.io/badge/Asana-273347?style=flat-square&logo=Asana&logoColor=white"/> <img src="https://img.shields.io/badge/Notion-000000?style=flat-square&logo=Notion&logoColor=white"/> <img src="https://img.shields.io/badge/Discord-5865F2?style=flat-square&logo=Discord&logoColor=white"/>

<br/>

> ## 해당 스택들을 사용한 목적을 간단히 알려주세요

- FrontEnd

  - React:
    - 다급한 사용자를 위해 한페이지에서 해결할 수 있도록 (UX)
    - 여러 중복되는 컴포넌트 재사용
    - 가상DOM으로 사용자 상호작용이 많은 페이지 성능 향상
    - CSR을 사용한 이유: 반려동물을 잃어버린 사람들이 필요에 따라 찾아와야하기 때문에 굳이 SEO를 고려하지 않아도 괜찮았다. 서버단에서 거리 계산이나 데이터 가져오기 등 부하가 많기 때문에 렌더링을 줄여서 서버에 부하를 줄여주는 게 좋아서 CSR로 구현

- BackEnd

  - 왜 nodejs와 express로 구축하셨나요? 그것만의 장점
  - 왜 mongoDB를 사용하셨나요? 관계형DB를 사용한다면 스키마가 더욱 간단하고 빠르지 않았을까요?
  - 왜 ngix와 pm2로 서버 환경을 세팅하셨나요?

- DataEngineer
  - Python
    - 문자열 및 데이터 처리에 편리하다.
    - 필요시 멀티스레드를 사용할 수 있다.
  - GCP
    - 무료 크레딧 이상으로 자동결제 되지 않는다.
    - 필요시 bigquery나 airflow를 구축할 수 있다.
    - 자동으로 특정시간 켜지고 꺼지도록 설정하는 방법을 알고 있어 크레딧을 아낄 수 있다.
  - crontab
    - Linux에 기본으로 있는 기본기능이라 설치하거나 설정하는 큰 번거로움이 없다.
    - Airflow와 달리 상태를 확인하기 어려운데 코드 실행시 각 단계를 자동으로 html에 write 하여 웹을 통해 상태를 살펴 볼수 있도록 구축했다.
  - Apach
    - APM setup 이라 불릴만큼 고전적이지만 익숙하고 기본적인 웹서버이기 때문이다.
  - twillio
    - 네이버 문자와 다르게 자동결제 되지 않는다.
    - 무료 크레딧으로 네이버 50건에 비해 약 300건 많은 발송이 가능하다.
    - 단 무료버전에서 문자를 받으려면 문자인증 과정이 필요하다.
  - 공공데이터 API
    - 대전지역 데이터가 더 정확하고 자세하지만 전국 데이터를 사용한 이유는 지역기반이 아닌 실종위치기반으로 서비스를 하기 위해서다. 중형견은 하루만에 몇십km를 달려 대전을 넘어간다.
