import threading
import time


ticket = 30

# 线程锁效率降低

# 创建一把锁
lock = threading.Lock()

def sell_tic():
    # ticket -= 1
    # if ticket <= 0:
    #     print('Piaomaiwanle')

    # 多个线程共享全局变量
    # 线程安全问题
    # 多线程是切换的 不是同时 因为时间很短所以显示为同时
    global ticket
    while True:
        lock.acquire()  # 加同步锁
        if ticket > 0:
            time.sleep(0.5)  # 单线程卖票
            ticket -= 1
            lock.release() # 加线程锁
            print('{}卖出一张还剩{}张\n'.format(threading.current_thread().name,ticket))
        else:
            lock.release() # 加线程锁
            print('meipiaole')

            break


# sell_tic()
t1 = threading.Thread(target=sell_tic,name='线程1')  # 线程1
t2 = threading.Thread(target=sell_tic,name='线程2')   # 线程2
# 多个窗口一起卖

t2.start()
t1.start()

