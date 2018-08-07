import socket
import os
sk = socket.socket()

address = ('127.0.0.1',8001)

sk.bind(address)

sk.listen(3)
path = r'E:\python\python_learn\网络编程\post'
while 1:
    print('等待客户端连接>>>>>>>>>>>>>>>>')
    conn, addr = sk.accept()
    print('当前连接客户端地址：{0}'.format(addr))
    while 1:
        data = conn.recv(1024)
        cmd,fileName,fileSize =str(data,'utf8').split(' ')
        fullPath = os.path.join(path,fileName)
        fileSize = int(fileSize)
        if cmd == 'post':
            f = open(fullPath,'wb')
            revOver = 0
            while revOver!=fileSize:
                data = conn.recv(1024)
                f.write(data)
                revOver +=len(data)
            f.close()
            conn.send(bytes('文件上传成功','utf8'))
        else:
            conn.send(bytes('指令不正确', 'utf8'))
