# Directory

https://codechacha.com/ko/python-walk-files/

# os.listdir()을 이용한 방법
````
import os

def print_files_in_dir(root_dir, prefix):
    files = os.listdir(root_dir)
    for file in files:
        path = os.path.join(root_dir, file)
        print(prefix + path)
        if os.path.isdir(path):
            print_files_in_dir(path, prefix + "    ")

if __name__ == "__main__":
    root_dir = "./test/"
    print_files_in_dir(root_dir, "")
````
위와 같이 재귀적으로 하는 방법이 있다. 그러나 파이썬은 최대 재귀한도를 1,000으로 제한하기 때문에 sys.setrecursionlimit(n)으로 재귀 한도를 1,000보다 높게 설정할 수 있지만 이는 segmentation fault를 일으킬 수 있기 때문에 추천되지 않는다.

# os.walk()를 이용한 방법
위와 유사한 구현 내용을 os.walk()로 처리할 수 있습니다.

os.walk()는 하위의 폴더들을 for문으로 탐색할 수 있게 해줍니다. 인자로 전달된 path에 대해서 다음 3개의 값이 있는 tuple을 넘겨줍니다.

- root : dir과 files가 있는 path
- dirs : root 아래에 있는 폴더들
- files : root 아래에 있는 파일들

예제는 다음과 같습니다. 모든 하위 폴더들에 대해서 for문이 실행되며, root는 그 폴더의 path가 됩니다. dirs와 files는 root 바로 밑에 있는 폴더와 파일들에 대한 리스트입니다.

````
import os

if __name__ == "__main__":
    root_dir = "./test/"
    for (root, dirs, files) in os.walk(root_dir):
        print("# root : " + root)
        if len(dirs) > 0:
            for dir_name in dirs:
                print("dir: " + dir_name)

        if len(files) > 0:
            for file_name in files:
                print("file: " + file_name)
````