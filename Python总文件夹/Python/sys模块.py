import sys  # x系统相关的功能
import random
import math
import datetime as dt
import calendar
import hashlib   # 用来数据加密的模块
import hmac
import tkinter
import pygame

pygame.pygame_dir
#sys
# print(math.factorial(10)) # 阶乘
# print(math.pow(2, 3)) # 幂运算
# round(2.6) #round是内置函数  不是Math里面的函数
#
# print(math.floor(12.98))  #向下取整
# print(math.ceil(12.98))  #向上取整

# random
print(random.randint(2, 9))

print(random.random()) #[0,1)之间的浮点类型的数

# # datatime(dt)
# print(dt.datetime.now())
# print(dt.date(2019, 12, 4))
#
#
# c = calendar.calendar(2019)
# print(c)

x = hashlib.md5()
x.update('zhouyu'.encode('utf8'))
print(x.hexdigest())  # c59156bcb92ade952bf51ce00f0e9b2d  没有解密的过程



