import io
from io import StringIO,BytesIO

# 将数据写入内存涉及到两类StringIO和BytesIO类

s_io = StringIO()
# s_io.write('hello  ')
# s_io.write('gong')
#
# # read 读不到
# print(s_io.getvalue())

# 将输出内容打印在文件里面
# print函数file参数是一个文件流  可以用这种方式打开 并用w写入
print('萨拉那个黑有',file=open('sss.txt','w'))

# 打印在内存里面
print('嘿嘿嘿哈哈哈',file=s_io)
print('急急急',file=s_io)
print('噢噢噢噢哦哦哦',file=s_io)

print(s_io.getvalue())

# 二进制格式的文件  encode编码  decode解码
b_io = BytesIO()
b_io.write('你好'.encode('utf8'))
print(b_io.getvalue().decode('utf8'))

s_io.close()
b_io.close()