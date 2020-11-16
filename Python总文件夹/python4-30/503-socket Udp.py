import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


# s.sendto('good'.encode('utf8'),('192.168.1.100',9999))
# ip = '110.18.27.176'
# port = 7890
s.bind(('110.18.27.176',9999))

data,addr = s.recvfrom(1024)

print('端口号是{}，ip地址是{}，收到的数据是{}'.format(addr[1],addr[0],data.decode('utf8')))


s.close()