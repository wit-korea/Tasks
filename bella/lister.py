import sys
import os
import random

# function define

def nomal_mode():
    print("nomal mode")
    for (path, dirs, files) in os.walk(sys.argv[1]):
    # print("# root : " + root)
        if len(dirs) > 0:
            for dir_name in dirs:
                print("dir: " + dir_name)

        if len(files) > 0:
            for file_name in files:
                print("file: " + file_name)

def random_mode():
    print("random mode")
    randList = []
    for (path, dirs, files) in os.walk(sys.argv[1]):
        if len(dirs) > 0:
            for dir_name in dirs: 
                randList.append(dir_name)

        if len(files) > 0:
            for file_name in files:
                randList.append(file_name)



    sampleList = random.sample(randList, len(randList))

    for i in sampleList:
        print(i)

# =====================================================
# main

length = len(sys.argv)
if length>2:
    option = sys.argv[2]


if length == 2:
    nomal_mode()
                

elif option == "random":
    random_mode()
    

elif option == "-ignore":
    print("ignore mode")
