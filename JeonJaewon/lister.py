from pathlib import Path
import sys, random
def main(argv):
    FILE_NAME = argv[0]
    PATH_NAME = argv[1]
    opt = ""

    # 전체 인자의 갯수 체크
    if len(argv) >= 3:
        opt = argv[2]

    pathObj = Path(PATH_NAME)
    arr = []
    tmpArr = []
    size = 0

    # 먼저 리스트에 넣는다
    for item in pathObj.glob('**/*'):
        arr.append(item)
        tmpArr.append(item)

    if opt == 'random':
        for i in range(len(arr)):
            rand = int(random.random() * len(arr))
            print(arr[rand])
            arr.remove(arr[rand])
    elif opt.startswith("ignore-"):
        optName = opt[7:]
        if optName.endswith('\\'):
            for i in range(len(arr)):
                if(str(arr[i]).startswith(PATH_NAME +'\\'+optName) or str(arr[i]) == (PATH_NAME +'\\'+optName[:-1])):
                    tmpArr.remove(arr[i])
        else:
            for i in range(len(arr)):
                if(str(arr[i]) == (PATH_NAME +'\\'+optName)):
                    tmpArr.remove(arr[i])
        for i in range(len(tmpArr)):
            print(tmpArr[i])

main(sys.argv)