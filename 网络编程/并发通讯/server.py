import socketserver

class mySevers(socketserver.BaseRequestHandler):

    def handle(self):
        while 1:
            conn = self.request
            addr = self.client_address
            print('已连接 {0} 客户端 \n'.format(addr[1]))
            while 1:
                data = conn.recv(1024)
                if not data:
                    print('当前客户端：{0} 已经断开连接'.format(addr[1]))
                    server.serve_forever()
                print('客户端{0}：{1}'.format(addr[1],str(data, 'utf8')))
                print('——————————————————————')
                inp = input('>>>>>>')
                conn.send(bytes(inp, 'utf8'))
                print('.' * 35 + 'Waiting' + '.' * 35 + '\n')
            conn.close()
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',6666),mySevers)
    print('>'*35+'服务器启动'+'<'*35+'\n')
    print('等待客户端连接'+'>'*10)
    server.serve_forever()