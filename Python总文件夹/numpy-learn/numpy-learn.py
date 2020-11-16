import numpy as np
import matplotlib.pyplot as plt



def tuple_learn():
    """
    学习元组的基本知识
    :return:
    """
    # value = 1,2,3,4,5,6
    # print(value)

    # a,b,*_ = value
    # print(*_)

    # sep = [(1,2,3),(4,5,6),(7,8,9)]
    # print(sep)
    # for a,b,c in sep:
    #     print('a = {0},b = {1},c = {2}'.format(a,b,c)) # 没理解 大概是要记下来

    # a = 1,2,3,56,6,6,6,5,8
    # print(a)
    # print(len(a))
    # print(a.count(6))

    a = tuple('string')
    print(a)

def list_learn():
    geb = range(10)
    print(geb)

    return

def numpy_learn():

    # data = {
    #     i : np.random.randn() for i in range(1,8)
    # }
    # print(data)

    # data = np.random.randn(3,6)
    # print(data,'\n',data.shape)

    # data2 = [[1,2,3,4],[5,9,6,5],['c',56,7,8]]
    # arr = np.array(data2)
    # print(arr.dtype)   #<U11
    # print(arr,arr.ndim)
    # arr.astype(np.float) could not convert string to float: 'c'
    #
    # arr2 = np.zeros((3,6))
    # print(arr2)

    # arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
    # print(arr2d[2,2])
    # arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
    # arr3d[0,1] = 42
    # print(arr3d)
    # print(arr3d[0,1])

    # str = 'abcdefghijkmlnopqrstuvwxyz'
    #
    # print(str[::-1])
    # data = np.arange(10)
    # print(data)
    # plt.plot(data)
    # plt.show()

    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    # ax1.show()
    arr = np.empty((8, 4))
    print(arr)
    for i in range(8):
        arr[i] = i
    print(arr)
    z = arr[[4,3,0,6]]
    print(z)




    return None


if __name__ == '__main__':
    # tuple_learn()
    # list_learn()
    numpy_learn()