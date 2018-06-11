__author__ = '財'

import os


def find_files(path, wanted):
    try:
        # 盘符内所有文件（夹）的路径
        dir_list = os.listdir(path)
        for filename in dir_list:
            # 当前文件（夹）的路径
            new_path = os.path.join(path, filename)
            # 如果是文件夹，深入下一级继续查找
            if os.path.isdir(new_path):
                find_files(new_path, wanted)
            # 若是文件，检查文件名里是否含有关键字, 应该不区分大小写，特别是针对后缀名时比较方便
            elif os.path.isfile(new_path):
                if wanted.lower() in filename.lower():
                    print(new_path)
    except Exception as e:
        print(e)


def save_all():
    p = input('path>>> ')
    k = input('key>>> ')
    find_files(p, k)


# if __name__ == '__main__':
#     save_all()

save_all()