# Ministagram

## TODO
- 계정 (1순위)
    - [x] 로그인
    - [ ] 회원가입
- 포스트 (2순위)
    - 피드
        - [x] 최신순 정렬이며, 특정 알고리즘을 적용해도 괜찮습니다.
        - [ ] 팔로우한 사람의 글과 내 글이 노출됩니다.
    - 작성
        - [x] 글 만 단독 작성은 불가능합니다.
        - [x] 삭제
        - [ ] 사진(최대 5장) 과 글을 동시에 작성
- 친구 (3순위)
    - [ ] 검색
    - [ ] 팔로우
    - [ ] 언팔로우

## Django Study
### manage.py
- `python manage.py migrate` : 생성된 프로젝트에 대한 데이터베이스 초기화
- `python manage.py startapp <app-name>` : appname라는 이름의 앱 생성(installed_app에 appname 추가)
- `python manage.py makemigrations <app-name>` : appname의 마이그레이션 파일 생성
- `python manage.py migrate <app-name>` : 마이그레이션 적용
- `python manage.py createsuperuser` : 관리자 계정 만들기
