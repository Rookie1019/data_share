import sys

# 了解
# sys.stdin     读取键盘里的内容 基本上等于input
# sys.stdout    标准输出
# sys.stderr    错误输出

s_in = sys.stdin # 拿到一个文件流 即一个文件对象

# while True:
#     content = s_in.readline().rstrip('\n')  # rstrip 去掉换行 在这时候if判断语句\n要换成''
#     if content == '\n': # 按第二下回车的时候结束程序
#         break
#
#     print(content)

sys.stdout = open('sss.txt','w',encoding='utf8') # 标准输出更改位置
print('sajdiw迪士尼打')

sys.stderr = open('sss.txt','w',encoding='utf8') # 错误输出更改位置
print(1/0)

# 输出
# Traceback (most recent call last):
#   File "C:/Users/13651/Desktop/Python/425-sys模块的使用.py", line 21, in <module>
#     print(1/0)
# ZeroDivisionError: division by zero