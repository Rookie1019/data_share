def nddd():
    print('调用了new')


def te(x, y):
    a = x // y
    b = x % y
    return (a,b)

#print(te(15,2))

re = te(320,3)

shang,yushu = te(80,3)

print('商是多少',shang)
print('余数是',yushu )





