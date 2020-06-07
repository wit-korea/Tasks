import os
import os.path
import sys
import random

file_list = []


def printList(list):
    for file in list:
        print(file)


def list_dir(path):
    for (root, dirs, files) in os.walk(path):
        if len(dirs) > 0:
            for dir_name in dirs:
                file_list.append(os.path.join(path, dir_name))
        if len(files) > 0:
            for file_name in files:
                file_list.append(os.path.join(path, file_name))


def list_dir_opt(path, opt):
    for (root, dirs, files) in os.walk(path):
        search_dir(root, dirs, files, opt, path)


def search_dir(root, dirs, files, opt, path):
    print("### root : ", root)
    if len(dirs) > 0:
        for dir_name in dirs:
            for option in opt:
                if dir_name in option:
                    if option.endswith("/"):
                        return
                else:
                    file_list.append(os.path.join(root, dir_name))
    if len(files) > 0:
        for file_name in files:
            for option in opt:
                if file_name in option:
                    if option.endswith("/"):
                        return
                else:
                    file_list.append(os.path.join(root, file_name))


def main():
    if len(sys.argv) == 2:
        PATH = sys.argv[1]
        list_dir(PATH)
        printList(file_list)

    elif len(sys.argv) == 3:
        PATH = sys.argv[1]
        OPT = sys.argv[2]
        if OPT.startswith("random"):
            list_dir(PATH)
            random.shuffle(file_list)
            printList(file_list)
        elif OPT.startswith("ignore"):
            option = OPT[7:].split('-')
            list_dir_opt(PATH, option)
            printList(file_list)


if __name__ == "__main__":
    main()
