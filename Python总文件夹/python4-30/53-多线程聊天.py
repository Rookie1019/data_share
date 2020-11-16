import socket
import threading


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('110.18.28.222',53276))
# s.sendto('good morning'.encode('utf8'),('192.168.1.105',8080))

file = open('聊天记录.txt','w',encoding='utf8')

def send_mes():
    while True:
        msg = input('输入内容:')
        s.sendto(msg.encode('utf8'), ('192.168.1.105', 8080))
        if msg == 'exit':
            break

def rec_mes():
    while True:
        data,addr = s.recvfrom(1024)
        print('从{}电脑{}端口接收到了{}'.format(addr[0],addr[1],
                                       data.decode('utf8')),file=file)

# print(data)

t1 = threading.Thread(target=send_mes)  # 线程1
t2 = threading.Thread(target=rec_mes)  # 线程1



s.close()