import math
import random

# 这是
# def cal(n):
#     if n == 0:
#         return n
#     else:
#         return n + cal(n-1)
#
# x = int(input('请输入数字：  '))
# # while True:
# print(cal(x))




# def max(*args):
#     x = args[0]
#     for arg in args:
#         if arg > x:
#             x = arg
#     return x
#
#
# print(max(1, 6, 8, 68, 95, 8599, 9485, 566))
# 这是判断大小的函数


def sum(n):

    m = 0
    for i in range(n):
        x = random.randint(1,6)
        m += x
        print(x)
    return m


print(sum(5))
# 求骰子的随机数和

def ssum(*args):
    x = 0
    for k in args:
        x += k
    return x/len(args)


print(ssum(1, 2, 3, 6, 5, 1))
#求平均数

def cap(word):
    c = word[0]
    if 'a'<= c <= 'z':
        new_str = word[1:]
        return c.upper() + new_str
    return word

print(cap('eloo'))
# 将首字母判断并大写


def endWith(word,isword):
    return word[-len(isword):] == isword


print(endWith('woshizhouyu', 'zhouyu'))
# 判断字符串是否以给定的字符串结尾

def isd(word):
    for k in word:
        if not ('9' >= k >= '0'):
            return False

    return True

print(isd('123'))
# 判断字符串是否为纯数字

def Change(word):
    new_str = ''
    for k in word:
        if 'z' >= k >= 'a':
            new_chr = chr(ord(k) - 32)
            new_str +=new_chr
        else:
            new_str +=k
    return new_str

print(Change('hefdsfSDSDda'))
# 将字母变成大写字母

def Replace(allword,old,new):
    # 用old把allword切开再把new加进去
    return new.join(allword.split(old))

print(Replace('how old are you','are','is'))
# 将语句里的固定部分换成另外一部分

def Max2(seq):
    if type(seq) == dict:
        seq = list(seq.values())
    x = seq[0]
    for i in seq:
        if i > x:
            x = i
    return x

print(Max2({'x': 15, 'y': 45, 'z': 101, 'da': 5}))
# 可以进行比较字典的value


