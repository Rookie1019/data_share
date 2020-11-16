# open函数打开文件
# 打开方式 mode 相对路径和绝对路径
# encoding 编码方式 windows系统默认gbk

# file = open('sss.txt','w',encoding='utf8')  # 默认rt格式打开     如果文件不存在会报错
# file.write('哇哇哇哇')
# file.close()

f = open('sss.txt',encoding='utf8')

# readline 只读一行
# while True:
#     content = f.readline()
#     print(content)
#     if content == '':
#         break
# print(f.readline())

# 读取多行  并存在于列表里

# print(f.readlines())

# print(f.read())
x = f.read(18) # 读取的长度 一般写成1024
print(x)
# print(f.read(3))

f.close()