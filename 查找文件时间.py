__author__ = '財'

import os
import datetime
dirs = input('请输入一个路径：')
files = os.listdir(dirs)
print('当前路径下的所有文件：\n',files)
print('='*50)
print('='*50)

name_times = {}
times_dir = []
#列出所有文件的创建时间
for i in files :
    path = os.path.join(dirs,i)
    times_dir.append(os.path.getctime(path))
#转成标准格式时间
for y in range(len(files)):
    format_times=datetime.datetime.fromtimestamp(times_dir[y])
    name_times[files[y]] =str(format_times) #给字典赋值，文件名是key，时间是value
maxs = max(name_times.values())
maxs_names = list(name_times.keys()) [list(name_times.values()).index(maxs)]
print('最新创建的名字: \t {0} \n创建时间为：\t{1} \n'.format(maxs_names , maxs[:-7]))
