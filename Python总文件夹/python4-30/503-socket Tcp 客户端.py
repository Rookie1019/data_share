import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 先和服务器连接
s.connect(('192.168.1.100',9999))

s.send('我是你爸'.encode('utf8'))

s.close()