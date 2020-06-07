import os

def search(dirname):
    try: #os.path.isdir()함수 호출시, 권한이 없는 디렉터리 접근 오류 처리
        filenames =os.listdir(dirname) #os.listdir: 해당 디렉터리에 있는 파일의 리스트
        for filename in filenames:
            full_filename=os.path.join(dirname,filename) #경로까지 보여주기
            if os.path.isdir(full_filename): #디렉터리인지, 파일인지 구별
                search(full_filename) #디렉터리일 경우 재귀호출로 하위 디렉터리까지 검색
            else:
                print(filename) #파일명만 출력
    except PermissionError:
        pass

def search2(dirname, path):
    try: #os.path.isdir()함수 호출시, 권한이 없는 디렉터리 접근 오류 처리
        filenames =os.listdir(dirname) #os.listdir: 해당 디렉터리에 있는 파일의 리스트
        for filename in filenames:
            full_filename=os.path.join(dirname,filename) #경로까지 보여주기
            if os.path.isdir(full_filename): #디렉터리인지, 파일인지 구별
                if flag==1 and path==filename:
                    break
                else:
                    search(full_filename) #디렉터리일 경우 재귀호출로 하위 디렉터리까지 검색
            else:
                if flag==2 and filename==path: #파일명 같지 않을 경우
                    continue
                else:
                    print(filename) #파일명만 출력
                
    except PermissionError:
        pass


flag=0;
check=[] #입력 리스트
str=input() #입력
check=str.split('-')

if check[0]=='random':
    flag=0
    search("c:/") #전체 경로 출력
elif check[0]=='ignore':
    if (check[1])[len(check[1])-1]=='/': #마지막이 /일 경우 하위폴더 제외
        flag=1
        search2("c:/",check[1])
    else: #해당 폴더만 출력 제외
        flag=2
        search2("c:/",check[1])
else:
    flag=3
    search(check[0])
   
        
