import threading
import queue
import time


def produce():
    for i in range(100):
        time.sleep(0.5)
        print('生产了++++++++{}个面包'.format(i))
        q.put('b{}'.format(i))

def customer():
    for i in range(100):
        time.sleep(0.5)
        x = q.get()

        print('买了--------{}个面包'.format(x))

q = queue.Queue() # 创建一个q
p1 = threading.Thread(target=produce,name='P1线程')
p2 = threading.Thread(target=customer,name='P2线程')

p1.start()
p2.start()
