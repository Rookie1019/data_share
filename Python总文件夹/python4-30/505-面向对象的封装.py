import socket


class Server(object):
    def __init__(self,ip,port):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((ip,port))
        self.socket.listen(128)

    def run(self):
        while True:
            client_socket, client_addr = self.socket.accept()

            data = client_socket.recv(1024).decode('gbk')

            response_header = 'HTTP/1.1 200 OK\n' + 'content-type:text/html\n'
            response_header += '\n'

            response_body = ''  # 默认是\ 为首页

            if data:  # 经常返回值为空  现在返回值如果有数据才切割 没有就不切割
                path = data.splitlines()[0].split(' ')[1]
                print('请求的数据是 ' + path)
                if path == '/login':
                    response_body = '欢迎来到登陆界面'
                elif path == '/register':
                    response_body = '欢迎来到注册界面'
                elif path == '/':
                    response_body = '欢迎来到首页'
                else:
                    response_body = '输入有误'
                    response_header = 'HTTP/1.1 404 Page Not Found\n' + 'content-type:text/html\n'

            client_socket.send((response_header + response_body).encode('gbk'))


s = Server('192.168.1.105',12581)
s.run()





