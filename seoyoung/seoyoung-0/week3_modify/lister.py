import os
import sys
import random

file_list=[]

def search(dir):
        files = os.listdir(dir)
        for file in files:
                fullFilename = os.path.join(dir, file)
                if os.path.isdir(fullFilename):
                        file_list.append(fullFilename)
                        search(fullFilename)
                else:
                        file_list.append(fullFilename)
                        


def searchTwo(dir,third):
        files = os.listdir(dir)
        for file in files:
            fullFilename = os.path.join(dir, file)
            if os.path.isdir(fullFilename):
                for ig in third:
                    if ig in fullFilename:
                            break
                    else:
                            if fullFilename.endswith(ig):
                                        searchTwo(fullFilename,third)
                                                      
            else:
                for ig in third:
                	if ig in fullFilename:
                        	break
                        else:
                        	file_list.append(fullFilename)

def print_list(list):
	for file_name in list:
            	print(file_name)


def main():
        if len(sys.argv) == 2:
                searchDir=sys.argv[1]
                search(searchDir)
                print_list(file_list)
        elif len(sys.argv) ==3:
                searchDir=sys.argv[1]
                second = sys.argv[2]
                if second =="random":
                        search(searchDir)
                        random.shuffle(file_list)
                        print_list(file_list)
                elif second.startswith("ignore"):
                        third=second[7:].split('-')
                        print(third)
                        searchTwo(searchDir, third)
                        print_list(file_list)
                        
                
if __name__ == "__main__":
    main()

