import os
import sys
import random

full_filename_list=[]  #파일의 디렉토리 경로 문자열들을 저장할 전역 변수

def search(dirname):            #모든 하위 디렉토리 검색 함수
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            full_filename_list.append(full_filename)
            #print("\t"*num+full_filename)
            if os.path.isdir(full_filename):
                search(full_filename)
    except PermissionError:
        pass

    return full_filename_list

def list_show(list):       #ist를 한줄씩 출력해주는 함수
    for element in full_filename_list:
        print(element)


######################

dirname = sys.argv[1]+" "+sys.argv[2]
full_filename_list = search(dirname)

if len(sys.argv)==3:
    list_show(full_filename_list)
elif len(sys.argv)==4:
    if(sys.argv[3]=="random"):
        random.shuffle(full_filename_list)
        list_show(full_filename_list)
    elif(sys.argv[3][0:7]):
        print("ignore 옵션")





