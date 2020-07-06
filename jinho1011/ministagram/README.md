# Ministagram
## Django Study
### manage.py
- `python manage.py migrate` : 생성된 프로젝트에 대한 데이터베이스 초기화
- `python manage.py startapp <app-name>` : appname라는 이름의 앱 생성(installed_app에 appname 추가)
- `python manage.py makemigrations <app-name>` : appname의 마이그레이션 파일 생성
- `python manage.py migrate <app-name>` : 마이그레이션 적용
- `python manage.py createsuperuser` : 관리자 계정 만들기

### accounts
- 장고에서는 기본적으로 로그인, 로그아웃 기능을 지원
- 전체적인 그림
  - urls.py를 만들어서 loginview와 logoutview를 바로 login.html과 logout.html로 전달
    - templates에 login.html과 logout.html 구현
  - models.py와 views.py를 거치지 않고 바로 구현 가능
  - 로그인 성공했을시 접속할 링크 구현
- urls.py로 바로 url 연결시켜주기


### 느낀점(?)
#### 장점
- 기본적으로 제공하는 것들이 많다 (Session, Admin, Security)
- 기본 언어가 **python**이다 (가장 큰 장점?)
- ORM
#### 단점
- 기본적으로 제공하는 것 이외의 커스텀이 힘들어 보임
  - photo앱을 만들고 models.py, views.py를 만지면서 느꼈음
  - 기본적으로 제공하는 것이 많기 때문에 전체적인 프레임워크 공부가 필요함 => 마음에 들지 않음.. (Top-Down과 Bottom-Up의 차이?)
- 비동기 지원 X
#### NodeJS와의 비교
> 장고는 완성된 거대한 모래성으로 겉부분을 파면서 필요없는건 버리고 필요한 것만 남겨놓고 작업  
> NodeJS는 아무것도 없고 레고처럼(?) 조립해야댐