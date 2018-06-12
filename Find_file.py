__author__ = '財'



import os
import subprocess
global search_files
search_files = []
class Find_file():
    def run(self,path , key):
        try:
            files = os.listdir(path)
            for file_names in files:
                new_full_path = os.path.join(path,file_names)
                if os.path.isdir(new_full_path) :
                    Find_file().run(new_full_path , key)
                elif os.path.isfile(new_full_path):
                    if key.lower() in file_names.lower():
                        print('【',len(search_files),'】',' ',new_full_path,'\n')
                        search_files.append(new_full_path)
        except Exception as Error_Infor:
            print(Error_Infor)
    def open_files(self,nums):
        if len(nums) == 0:
            pass
        else:
            subprocess.Popen(search_files[int(nums)],shell=True)

s_dir = input('请输入路径：')
s_key = input('请输入关键词：')
Find_file().run(s_dir,s_key)
Find_file().open_files(input('想要打开哪个文件，输入序号（回车默认不打开任何文件）：'))







