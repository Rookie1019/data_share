import threading
import time
import requests
#
# def dance():
#     for k in range(50):
#         print('我在跳舞')
#         time.sleep(1)
#
# def sing():
#     for k in range(50):
#         print('我在唱歌')
#
# # sing()
# # dance()
#
# # target需要函数 用来指定线程需要执行的任务
# t1 = threading.Thread(target=dance)  # 线程1
# t2 = threading.Thread(target=sing)   # 线程2
#
# t1.start()
# t2.start()

e = requests.get('https://www.bilibili.com/video/BV1jE411x7ss?p=264')
print(e.text)
print(e.json())