# import mmap
#
# muuu = lambda a,b:a * b
#
# print(muuu(4, 3))

def test(a,b,fn):
     return fn(a,b)


# def add(a,b):
#     return a + b
# def min(a,b):
#     return a - b
#
# # 回调函数 （把函数当作另外一个函数的参数）
# print(test(3, 2, add))# 这里的fn = add  且只是add  函数名  不能加括号
# print(test(3, 2, min))

x1 = test(8,9,lambda a,b:a + b)
x2 = test(8,9,lambda a,b:a - b)
x3 = test(8,9,lambda a,b:a * b)
x4 = test(8,9,lambda a,b:a / b)

print(x1)
print(x2)
print(x3)
print(x4)