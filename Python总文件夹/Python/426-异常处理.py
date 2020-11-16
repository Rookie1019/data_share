
def dix(a,b):
    return a/b

try:
    x = dix(5,0)
except Exception as e:
    print('程序出错')
else:
    print(x)