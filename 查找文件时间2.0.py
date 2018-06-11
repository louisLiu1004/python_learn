__author__ = '財'

import os
import datetime
dirs = input('请输入一个路径：')
files = os.listdir(dirs)
print('当前路径下的所有文件：\n',files)
print('='*50)
print('='*50)



times_dir = [os.path.join(dirs,i) for i in files] #列出所有文件的创建时间
times_dir.sort(key=os.path.getctime)
print('最新创建的名字：',os.path.basename(times_dir[-1]))
print('创建时间为：',str(datetime.datetime.fromtimestamp(os.path.getctime(times_dir[-1])))[:-7]) #转成标准格式时间



