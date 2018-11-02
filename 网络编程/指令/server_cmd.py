import socket
import subprocess
sk = socket.socket()

address = ('127.0.0.1',8001)

sk.bind(address)

sk.listen(3)

while 1:
    print('等待客户端连接>>>>>>>>>>>>>>>>')
    conn, addr = sk.accept()
    print('当前连接客户端地址：{0}'.format(addr[1]))
    while 1:
        try:
            data = conn.recv(1024)
            if not data:
                print('当前客户端：{0} 已经断开连接'.format(addr[1]))
                break
        except Exception:
            break
        print('客户端命令>>>>> {0}'.format(str(data,'utf8')))
        action = subprocess.Popen(str(data,'utf8'),shell=True,stdout=subprocess.PIPE)
        result = action.stdout.read()
        result_len = bytes(str(len(result)),'utf8')
        conn.sendall(result_len)
        conn.recv(1024)
        conn.sendall(result)
