import re
# /d

nums = input('qingshuru\n')
if re.fullmatch(r'\d+\.?\d+',nums):
    print(float(nums))
else:
    print('不是数字')



