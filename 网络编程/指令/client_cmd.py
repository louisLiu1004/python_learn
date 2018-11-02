import socket

sk = socket.socket()

address = ('127.0.0.1',8001)
sk.connect(address)
while 1:
    inp = input('请输入命令>>>>>>')
    if inp =='exit':
        print('即将断开连接，确认：1,取消：0')
        creat = input('请输入>>>')
        if creat == '1':
            print('断开连接')
            break
        else:
            print('已取消,保持连接')
    sk.send(bytes(inp,'utf8'))
    result_len = int(str(sk.recv(1024),'utf8'))
    sk.send(bytes('ok','utf8'))
    data = bytes()
    while len(data) != result_len:
        data+=sk.recv(1024)
    print('服务器：{0}'.format(str(data,'gbk')))

