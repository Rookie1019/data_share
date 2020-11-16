import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([1.0, 2.0, 3.0])
y_data = np.array([2.0, 4.0, 6.0])

np.random.randint()
np.arange()
def generate():
    for x in range(10):
      yield x
Z = np.fromiter(generate(), dtype=float, count=-1)
np.random.random()


def course(x, w):
    """ 无偏置的情况"""
    return x * w


def loss(x, y, w):
    """损失函数 （最小二乘法）"""
    y_p = course(x, w)
    return (y_p - y) ** 2


def cal():
    w_list = []
    MSE_list = []
    for w in np.arange(0.0, 4.0, 0.1):
        print(w)
        l_sum = 0
        for x_val, y_val in zip(x_data, y_data):
            loss_val = loss(x_val, y_val, w)
            l_sum += loss_val
            # print(l_sum)
        w_list.append(w)
        MSE_list.append(l_sum / 3)
        # print(MSE_list)
    plt.plot(w_list, MSE_list)
    plt.ylabel('loss')
    plt.xlabel('w')
    plt.show()


cal()
