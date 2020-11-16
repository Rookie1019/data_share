import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('110.18.27.176',9999))
x = s.listen(128) # 被动监听
print(x)
s.accept()