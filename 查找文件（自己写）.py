__author__ = '財'


import os
import  threading

def Find_file (path , key ):
    try:
        files = os.listdir(path)
        for file_names in files:

            new_full_path = os.path.join(path,file_names)
            if os.path.isdir(new_full_path) :
                Find_file(new_full_path,key)
            elif os.path.isfile(new_full_path):
                if key.lower() in file_names.lower():
                    print(new_full_path)
    except Exception as Error_Infor:
        print(Error_Infor)


Find_file(input('PATH:'),input('KEY:'))