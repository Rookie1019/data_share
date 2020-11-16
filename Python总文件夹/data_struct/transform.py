# 十进制转到二进制
# 转换为其他进制就是 除以2变成除以n
# from data_struct import data_opera
from data_struct.data_opera import Stack


def divide2(num:int):
    s = Stack()
    
    # if 0 <= num <= 2:
    #     return 1
    # else:
    #     res = num % 2
    #     s.push(res)
    #     ss = num // 2
    while num > 0:
        res = num % 2
        s.push(res)
        num = num // 2
        print(res)
        
    binstring = []
    while not s.isEmpty():
        binstring.append(s.pop())
    return binstring


def divide_n(num, base):
    digits = '0123456789ABCEDF'
    s = Stack()
    
    while num > 0:
        res = num % base
        s.push(res)
        num = num // base
        # print(res)
        
    binstring = []
    while not s.isEmpty():
        binstring.append(s.pop())
    return binstring

def turn(n):
    stack = Stack()

    while n!=0:
        m=n%2
        stack.push(m)
        n=n//2
    x=''
    for i in range(stack.size()):
        pp=stack.pop()
        x = x + str(pp)
    return x

    

if __name__ == "__main__":
    # print(divide2(233)) 
    print(turn(233))