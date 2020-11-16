import requests
import threading

import re
re = requests.get('http://192.168.43.64:12138')
# 拿到一个response对象
# print(re)


print(re.content.decode('utf8'))
# content是一个二进制结果 可以包括图片 和text区分

print(re.text) # 拿到的就是一个字符串
print(re.status_code) # 拿到状态码

print(re.json()) # 将字符串解析成python里面的数据（字典格式（json格式））