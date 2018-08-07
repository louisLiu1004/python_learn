import socket
import os
from tqdm import tqdm
import math
sk = socket.socket()

address = ('127.0.0.1',8001)
sk.connect(address)
while 1:
    inp = input('请输入上传文件路径>>>>>>') #post 路径
    if inp =='exit':
        print('即将断开连接，确认：1,取消：0')
        creat = input('请输入>>>')
        if creat == '1':
            print('断开连接')
            break
        else:
            print('已取消,保持连接')
    cmds,path = inp.split(' ')
    fileName = os.path.basename(path)
    fileSize = os.stat(path).st_size
    fileInfo = 'post {0} {1}'.format(fileName,fileSize)
    sk.sendall(bytes(fileInfo,'utf8'))

    f=open(path,'rb')
    sentOver = 0
    for i in  tqdm(range(math.ceil(fileSize/1024))):
    # while sentOver!=fileSize:
        data = f.read(1024)
        sk.sendall(data)
        sentOver +=len(data)
    f.close()
    print(str(sk.recv(1024),'utf8'))


