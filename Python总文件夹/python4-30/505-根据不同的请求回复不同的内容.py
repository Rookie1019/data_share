# HTTP协议 超文本传输协议
# 用来传输超文本的
import socket

# HTTP 服务器都是基于TCP的socket的连接
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('192.168.1.105',12581))
# server_socket.bind(('0.0.0.0',12581))  # 更多的绑定是通过0.0.0.0
# 绑定127.0.0.1 只能通过本机访问

server_socket.listen(128)

# 获取到一个元组
# 第一个元素是 客户端的socket连接
# 第二个元素是 客户端的ip地址和端口号
#     x = server_socket.accept() # 拿到一个元组
#     print(x)


client_socket,client_addr = server_socket.accept()
# 从客户端的 socket 里面获取数据
data = client_socket.recv(1024).decode('gbk')
# print(data)  # 客户端的请求值


# # 返回内容之前 先设置HTTP响应头
# client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8')) # 响应头 必须的
# client_socket.send('content-type:text/html\n'.encode('utf8'))
# # client_socket.send()
# client_socket.send('\n'.encode('utf8')) # 换行  所有的响应头设置完 再换行


response_header = 'HTTP/1.1 200 OK\n' + 'content-type:text/html\n'
response_header += '\n'
# 请求头
# 请求体
response_body = '' # 默认是\ 为首页
# client_socket.send((response_header+response_body).encode('gbk'))
if data:  # 经常返回值为空  现在返回值如果有数据才切割 没有就不切割
    path = data.splitlines()[0].split(' ')[1]
    print('请求的数据是 '+path)
    if path == '/login':
        response_body = '欢迎来到登陆界面'
    elif path == '/register':
        response_body = '欢迎来到注册界面'
    elif path == '/':
        response_body = '欢迎来到首页'
    else:
        response_body = '输入有误'
        response_header = 'HTTP/1.1 404 Page Not Found\n' + 'content-type:text/html\n'

client_socket.send((response_header+response_body).encode('gbk'))


# 设置颜色
# client_socket.send('<h1 style="color:red">陶凤磊</h1>'.encode('gbk'))

# 向客户端发送内容
# client_socket.send('陶凤磊'.encode('gbk'))