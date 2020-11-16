# 序列化和反序列化  dumps loads

import json

names = ['sorr','李四','王五','赵六']  # 汉字的格式会输出编码格式
# 注意dump和dumps的差别
# dumps的作用是将数据转换成字符串
# dump将数据转换成为字符串的同时写入到指定文件  不需要再手动写入
# x = json.dump(names)


print('    ')
# x = json.dumps(names)  # dumps的作用是将数据转换成字符串



file = open('sss.txt','w',encoding='utf8')
# file.write(x)
#
# file.close()
y = json.dump(names,file)

z = json.loads()