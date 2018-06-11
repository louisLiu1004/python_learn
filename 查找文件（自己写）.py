__author__ = '財'



import os
global search_files
search_files = []
class Find_file():
    def run(self,path , key):
        try:
            files = os.listdir(path)
            nums = 0
            for file_names in files:
                new_full_path = os.path.join(path,file_names)
                if os.path.isdir(new_full_path) :
                    Find_file.run((new_full_path , key))
                elif os.path.isfile(new_full_path):
                    print(nums ,'.',new_full_path)
                    nums += 1
                    search_files.append(new_full_path)
            Find_file().open_files(input('想要打开哪个文件，输入序号（回车默认不打开任何文件）：'))
        except Exception as Error_Infor:
            print(Error_Infor)

    def open_files(self,nums):
        if len(nums) == 0:
            pass
        else:
            os.system(search_files[int(nums)])


Find_file().run(input('请输入路径：'),input('请输入关键词：'))







