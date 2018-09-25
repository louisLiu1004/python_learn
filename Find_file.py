<<<<<<< HEAD
# __author__ = '財'
#
#
#
# import os
# global search_files
# search_files = []
# class Find_file():
#     def run(self,path , key):
#         try:
#             files = os.listdir(path)
#             for file_names in files:
#                 new_full_path = os.path.join(path,file_names)
#                 if os.path.isdir(new_full_path) :
#                     Find_file().run(new_full_path , key)
#                 elif os.path.isfile(new_full_path):
#                     if key.lower() in file_names.lower():
#                         print(len(search_files),'.',new_full_path)
#                         search_files.append(new_full_path)
#
#         except Exception as Error_Infor:
#             print(Error_Infor)
#     def open_files(self,nums):
#         if len(nums) == 0:
#             pass
#         else:
#             os.system(search_files[int(nums)])
#
# s_dir = input('请输入路径：')
# s_key = input('请输入关键词：')
# Find_file().run(s_dir,s_key)
# Find_file().open_files(input('想要打开哪个文件，输入序号（回车默认不打开任何文件）：'))
#

a = r' J:\教程\特效教程\Maya灰飞烟灭特效动画实例训练视频教程\视频教程\50 - Simulate a Dry Sand Effect Using nParticles and nConstraints - Exploring nConstraints Attributes.mp4'
b = []
b.append(a)
print(b[0])
=======
__author__ = '財'

import os
import subprocess
# 导入模块

global search_files
search_files = []
# 定义变量
class Find_file():
    def run(self, path, key):
        try:
            files = os.listdir(path) #列出路径内所有文件名
            for file_names in files:
                new_full_path = os.path.join(path, file_names)
                if os.path.isdir(new_full_path):  #判断是否是文件夹
                    Find_file().run(new_full_path, key)
                elif os.path.isfile(new_full_path):  #判断是否是文件
                    if key.lower() in file_names.lower():  #判断是否包含关键字
                        print('【', len(search_files), '】', ' ', new_full_path, '\n')
                        search_files.append(new_full_path)
        except Exception as Error_Infor:
            print(Error_Infor)

    def open_files(self, nums):
        if len(nums) == 0:
            pass
        else:
            subprocess.Popen(search_files[int(nums)],shell=True)

s_dir = input('请输入路径：')
s_key = input('请输入关键词：')
Find_file().run(s_dir,s_key)

while True:
    if len(search_files) > 0:
        Find_file().open_files(input('想要打开哪个文件，输入序号（回车默认不打开任何文件）：'))
    else:
        print('==========【没找到相关文件】=========')
        s_key = input('请重新输入关键词：')
        Find_file().run(s_dir,s_key)






>>>>>>> origin/master
