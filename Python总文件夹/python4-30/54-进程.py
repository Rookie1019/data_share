import multiprocessing
import os
import time

def dance(n):
    for k in range(n):
        time.sleep(0.5)
        print('正在跳舞,pid={}'.format(os.getpid()))

def sing(n):
    for k in range(n):
        time.sleep(0.5)
        print('正在唱歌,pid={}'.format(os.getpid()))

# windows电脑直接启动会报错 必须用main函数启动py文件
# p1 = multiprocessing.Process(target=dance)
# p2 = multiprocessing.Process(target=sing)
#
# p1.start()
# p2.start()

if __name__ == '__main__':
    # 创建了两个进程
    # target是目标函数
    # args 用来传参  是个元组
    p1 = multiprocessing.Process(target=dance,args=(50,))
    p2 = multiprocessing.Process(target=sing,args=(50,))

    p1.start()
    p2.start()

# a = 10
# b = 10
# print(id(a)) # 1388640320
# print(id(b)) # 1388640320