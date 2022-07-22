# openApi_rescue

openapi_upr_cd.py -> 시도 코드 불러오기

openapi_org_cd.py -> 시군구 코드 불러오기

openapi_kind.py -> 품종 코드 불러오기

openapi_care_reg_no.py -> 보호소 코드 불러오기

openapi.py -> 보호 동물 불러오기

shelter.py -> 보호소 정보 불러오기

> <img width="600" alt="before1" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4aed5f10-d70f-44fc-b887-bc538296a113/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T104941Z&X-Amz-Expires=86400&X-Amz-Signature=ad918a86c21dd7fd46260dfebcee3df21a0e2f6880d457b90330103fd6a7e30b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject">
> <br />

# 구해줘 댕냥스 🐶🐱

> 잃어버린 우리 댕냥이<br />
> 하루종일 보호소 공고 확인하셨다구요?<br />
> 보호소에서 찾는건 <b>구해줘 댕냥스</b>에게 맡겨주세요!🔍<br />
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
  - 전체 분실 목록
  - 마이페이지
  - 관리자 페이지
  - 페이지 네이션
  - 목록 지도 전환 토글 기능
  - 필터 기능
    <br/>

### [구해줘 댕냥쓰 보러 가실까요!](http://kdt-sw2-seoul-team04.elicecoding.com/)

<br/>

> ## Figma
>
> <br/>
> <img width="600" alt="before1" src="https://i.ibb.co/bLKMnLq/image.png">

[Figma Link](https://www.figma.com/file/8QNY0Il76dIr7fUDNXhkjz/2nd-Project-Rescue-Puppy-Kitten?node-id=0%3A1)

<!-- <iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2F8QNY0Il76dIr7fUDNXhkjz%2F2nd-Project-Rescue-Puppy-Kitten%3Fnode-id%3D0%253A1" allowfullscreen></iframe> -->

> ## 스토리보드 및 유저 시나리오

- 사용자는 로그인하면 햄버거 메뉴의 분실등록으로 이동한다.
- 사용자는 분실등록에서 분실정보를 기입하고 게시글을 등록할 수 있다.
- 사용자는 분실목록에서 모든 사용자 전체 분실글을 확인할 수 있다.
- 사용자는 마이페이지에서 개인정보 수정, 본인 분실신고 리스트, 계정탈퇴를 할 수 있다.
- 사용자는 마이페이지에서 분실신고 리스트에서 분실 게시글 상세를 확인하고 수정 할 수 있다.
- 사용자는 메인 페이지 및 햄버거메뉴 구조리스트에서 보호소에서 올라온 공고들을 확인할 수 있다.
- 사용자는 메인 페이지 및 햄버거메뉴 구조리스트에서 보호소에서 올라온 공고들을 종별로 필터링 할 수 있다.
- 사용자는 메인 페이지 지도보기 버튼 토글 및 햄버거메뉴 구조지도에서 보호소에서 지도 페이지로 전환 할 수 있다.
- 관리자는 관라자페이지에서 회원정보관리, 분실신고 리스트 확인을 할 수있다.
- 관리자는 회원정보 관리에서 회원을 삭제할 수 있다.
- 관리자는 분실 신고 리스트에서 분실신고를 삭제할 수 있다.

<br/>

> ## 구현 기능 명세
>
> <br/>

#### 1. 메인페이지-구조 목록

<br/>

<img width="600" alt="before1" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7396416d-32dc-4575-89bd-7f5e08de49c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T045935Z&X-Amz-Expires=86400&X-Amz-Signature=e6ece64d1ad4cb4a82d92c3ca6d25c64d7c4f93c1ae3ad9eaab45e129a7ba1df&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject">

    1.1 사용자가 선택한 개수씩 목록 보기

    1.2 페이지네이션 적용

    1.3 동물 종류에 따른 체크박스 필터 기능

    1.4 구조 목록-구조 지도 전환 토글 버튼

    1.5 반응형 페이지 디자인

<br/>

#### 2. 회원가입, 로그인 페이지

<br/>

<img width="600" alt="before1" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6eefe2cc-c835-4ce1-89be-6cbc24c0602a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T045942Z&X-Amz-Expires=86400&X-Amz-Signature=6493c8c46acd82321ed7565dc6d7116e0b211061f632fd8e692eae2fddf3ac16&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject">
<img width="600" alt="before1" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9a019220-218d-4778-91f0-c70f2963a603/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T045946Z&X-Amz-Expires=86400&X-Amz-Signature=61c21d19aa379bd508e15bf8219437f784dae20adcd6c0c3783732a9e2cf05ed&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject">

    2.1 아이디, 비밀번호, 전화번호 유효성 검증

    2.2 관리자계정 별도 관리

    —> 로그인한 계정에 따라 마이페이지 연결시 일반회원>마이페이지 관리자>관리자페이지 연결

<br/>

#### 3. 마이페이지

<br/>

<img width="600" alt="before1" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/bdbfa09c-1b3b-4d2f-8bd6-9ba561c9c75b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T045949Z&X-Amz-Expires=86400&X-Amz-Signature=7972ddd845e4d7e708522d3f4ee0c08a0dff6abd0a21ce94b7eb5089c8650bbf&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject">

    3.1 회원정보 수정 유효성 검증

    3.2 본인이 등록한 분실 신고목록 상태변경, 삭제, 상세보기 가능

    3.3 계정 탈퇴 가능

    —> 비밀번호 일치여부에 따라 계정 삭제 가능

<br/>

#### 4. 관리자페이지

<br/>

<img width="600" alt="before1" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1e867431-6f1d-4c68-982f-3413dbe7905f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T045954Z&X-Amz-Expires=86400&X-Amz-Signature=553fc794459615027f0b2c34d07693e9b5724e8e7041e087b1676b0963a28f92&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject">

    3.1 모든 회원정보 확인 가능

    3.2 신고된 분실목록 전체 조회 가능

<br/>

#### 5. 분실 등록

<br/>

<img width="600" alt="before1" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/497ef6af-7d8b-4ca0-9ff0-3d48f288eb94/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T045957Z&X-Amz-Expires=86400&X-Amz-Signature=a58c04d277136b8434514872d85c02384b6c1862c324775cca745df8dca7dce0&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject">

    4.1 카카오 지도를 이용하여 분실 위치 받기

    4.2 위,경도로 받은 분실 위치를 주소로 변환하여 사용자에게 나타내기

    4.3 사진 서버에 저장

    4.4 분실 등록 삭제

    4.5 분실 등록 수정

<br/>

#### 6. 분실 상세

<br/>

<img width="600" alt="before1" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/20da20ac-035f-4527-9600-9e05b786194e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T050001Z&X-Amz-Expires=86400&X-Amz-Signature=87e0b75e74373029eca192afe9db66383117a7b7cead3289cf5b51daed2b3679&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject">

<br/>

#### 7. 구조 지도

<br/>

<img width="600" alt="before1" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/65ee0cf6-bc30-414b-92f3-84b49366a497/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T050004Z&X-Amz-Expires=86400&X-Amz-Signature=63f0f970e8f1acb7dc7ba25851d4bbb38a1e5049954b073e556789910b36607d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject">

    7.1 현재 위치 기준으로 주변의 구조된 동물 발견 위치 맵핑(카카오 map api 사용)

    7.2 info window로 구조 사진 및 간단한 정보 표시

<br/>

#### 8. 기타

<br/>

    8.1 localStorage에 token 저장하여 로그인 시 nav바 메뉴 변경

    8.2 sticky header와 hamburger menu 적용

    8.2 근처에 구조된 새로운 내역이 있다면 SMS으로 알림 표시 (twilio 사용)

    8.3 데이터 파이프라인 실시간 현황 페이지

    8.4 문자 알림

<br/>

##### 데이터 파이프라인 실시간 현황 웹페이지

<img width="600" alt="before1" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7a5a4a29-b07e-4acc-a0cc-e111003ff78d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T050008Z&X-Amz-Expires=86400&X-Amz-Signature=230fbf96ef512ad9cc88643ff13d9eb0553542a0638ef773e1c388c61b0eccbe&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject">

#### [데이터 파이프라인 실시간 현황 페이지](http://34.83.15.156/)

<br/>

##### 문자알림

<img width="600" alt="before1" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/394fb85c-bfc6-4870-aec3-725fbdf4f3c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T023953Z&X-Amz-Expires=86400&X-Amz-Signature=2c7d981ca7a4d2ba70c5db243404031071fed5cf24fcdebafe531a27a52b9292&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject">
<br/>

<br/>

> ## 실행방법

```bash
@~project-templet> npm install --global yarn
@~project-templet> npm install && yarn setup # yarn setup는 client server 각 폴더에 자동으로 패키지를 설치하는 사용자 정의 명령어입니다.
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

- React:
  - 다급한 사용자를 위해 한페이지에서 해결할 수 있도록 (UX)
  - 여러 중복되는 컴포넌트 재사용
  - 가상DOM으로 사용자 상호작용이 많은 페이지 성능 향상
  - CSR을 사용한 이유: 반려동물을 잃어버린 사람들이 필요에 따라 찾아와야하기 때문에 굳이 SEO를 고려하지 않아도 괜찮았다. 서버단에서 거리 계산이나 데이터 가져오기 등 부하가 많기 때문에 렌더링을 줄여서 서버에 부하를 줄여주는 게 좋아서 CSR로 구현
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
  - APM setup 이라 불릴 만큼 고전적이지만 익숙하고 기본적인 웹서버이기 때문이다.
- twillio
  - 네이버 문자와 다르게 자동결제 되지 않는다.
  - 무료 크레딧으로 네이버 50건에 비해 약 300건 많은 발송이 가능하다.
  - 단 무료버전에서 문자를 받으려면 문자인증 과정이 필요하다.
- 공공데이터 API
  - 대전지역 데이터가 더 정확하고 자세하지만 전국 데이터를 사용한 이유는 지역기반이 아닌 실종위치기반으로 서비스를 하기 위해서다. 중형견은 하루만에 몇십km를 달려 대전을 넘어간다.

</br>

> ## 팀원 역할
>
> <br/>

| 이름   | 역할                                                                  | 구현 기능                                                                                                     |
| ------ | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| 황채림 | <img src="https://img.shields.io/badge/FE-06B6D4?style=flat-square"/> | 헤더,햄버거 메뉴, 메인페이지, 구조리스트,필터, 페이지네이션, 목록 <->지도 전환 토글                           |
| 김재민 | <img src="https://img.shields.io/badge/FE-06B6D4?style=flat-square"/> | 데이터 pipeline 서버 구축, 문자서비스, 지도 페이지, 로그인, 회원가입 페이지, API(보호소코드, 보호소별 동물수) |
| 김소리 | <img src="https://img.shields.io/badge/FE-06B6D4?style=flat-square"/> | 분실등록 위치, 사진 등록 기능, 분실동물 상세 정보 불러오기, 구조동물 상세페이지, 지도 페이지                  |
| 임연주 | <img src="https://img.shields.io/badge/FE-06B6D4?style=flat-square"/> | 개인정보 수정, 계정 탈퇴, 분실목록 불러오기, 관리자페이지, 회원가입, 로그인                                   |
| 이진서 | <img src="https://img.shields.io/badge/BE-000000?style=flat-square"/> | 로그인, 회원가입, 구조동물, 분실동물 관련, 데이터 구축, 서버연결                                              |

<br/>
                                            |

<br/>

> ## 개발 과정에서 마주친 어려움, 해결방법, 결과

<br/>

- <img src="https://img.shields.io/badge/FE-06B6D4?style=flat-square"/> 재민 : 장소데이터가 정확하지 않아 kakao map api를 통해 위경도 좌표로 변환하는 과정이 어려웠습니다. 장소는 해당 장소 키워드가 포함된 15개 장소를 반환 받아 평균 좌표로 중간 좌표를 산출해내는 방식을 사용했습니다. 장소검색(place2coords)이 되지 않을 경우 보호소 주소를 바탕으로 주소검색(address2coords)을 통해 위경도로 표시했고 주소에서 시, 도 명을 추출하여 장소 검색으로 어떻게든 해보려 했지만 안되는 경우 포기하고 독도로 표기해두었습니다. 나중에는 정규표현식을 공부하여 개선하고 싶습니다.
  <br/>

  - 예를 들어 주소검색을 통해 서울특별시 어쩌구 저쩌동 100-1 이 없는 주소일 경우 정규식을 통해 서울특별시/도, 어쩌구/시/읍/군, 저쩌동/리을 분리하여 세부 지역 부터 장소검색을 할것입니다.

<br/>

- <img src="https://img.shields.io/badge/FE-06B6D4?style=flat-square"/> 채림 : 구조리스트 필터 구현할 때 필터 컴포넌트와 리스트 컴포넌트 간 state 공유에 어려움이 있었습니다. 상위 컴포넌트를 만들어 state 끌어올리기를 하려고 했으나 fetch 과정에서 처음의 빈 데이터 리턴이 props로 넘어가는 문제가 있었습니다. useFetch 커스텀 훅을 만들려고 했으나 [오피스아워 이슈] 이유로 실패했고 필터 컴포넌트 내부에서 fetch받아서 하위의 리스트 컴포넌트의 props로 넘겨서 해결하였습니다.

<br/>

- <img src="https://img.shields.io/badge/BE-000000?style=flat-square"/> 진서 : 구조동물 모두 비교가 아니라 보호소 비교 이슈로 기획 축소했던 부분이 있었습니다. 알림 서비스를 구현하는 과정에서 분실한 위치를 입력 받은 후에 등록된 모든 구조동물의 위치와 비교하려 하였습니다. 하지만 너무 오랜 시간이 예상 되어 구조된 동물이 보호되고 있는 보호소 위치와 비교하는 방식으로 기획 수정하였습니다.

<br/>

- <img src="https://img.shields.io/badge/FE-06B6D4?style=flat-square"/> 연주 : 유저 정보를 불러오는 api를 페이지마다 중복으로 불러와야했는데 context api를 쓰다보니 페이지를 새로고침 할 때마다 로그아웃되는 문제가 있었습니다. 유저관련 api모듈을 만들어서 필요할 때 마다 데이터를 불러오는 식으로 해결할 수 있었습니다.

<br/>

- <img src="https://img.shields.io/badge/FE-06B6D4?style=flat-square"/> 소리 : 분실동물을 등록할 때 사용자 위치를 등록하는 기능 개발에 어려움이 있었습니다. 위경도를 주소로 바꿔주는 카카오 지도 api를 사용했습니다. 끝내 카카오 dev console에서 사용자의 ip를 모두 허용해야 등록되어야 해당 api를 사용할 수 있다는 것을 알고 해결했습니다. 사진 등록 시 사진등록 컴포넌트와 상위 컴포넌트끼리 state를 공유하는 것에 문제가 생겨서 사진등록에 어려움을 겪었으나 하위 컴포넌트로 props를 넘겨서 해결하였습니다.
