from math import *


def Gini_single(a,b):
    single_gini = 2*((a*b)/(a+b)**2)
    return round(single_gini,2)

def Gini_index(a,b,c,d):
    zuo = Gini_single(a,b)
    you = Gini_single(c,d)

    total = a + b + c + d
    g_index = zuo*((a+b)/total) + you*((c+d)/total)
    return round(g_index,2)

if __name__ == '__main__':
    c = Gini_single(37,127)
    gini_index = Gini_index(37,127,100,33)
    print(c)
    print('总的基尼指数为 :',gini_index)  #总的基尼指数为 : 0.36