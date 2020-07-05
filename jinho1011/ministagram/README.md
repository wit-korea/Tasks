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