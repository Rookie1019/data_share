import numpy as np
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)





def fib(n):

    if n < 3:
        return 1
    return fib(n-2) + fib(n-1)
    # 时间复杂度是O(n)



def fib_num(n):

    tem = np.zeros(n)
    tem[0] = 1
    tem[1] = 1
    for i in range(2,n):
        tem[i] = tem[i-1] + tem[i-2]
    return tem
    



if __name__ == "__main__":
    # print(fib(40))
    c = fib_num(6)
    print(c)
    

