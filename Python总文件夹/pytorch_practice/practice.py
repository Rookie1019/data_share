import torch
import numpy as np


def flatten(t:torch.tensor):
    t = t.reshape((1,-1))
    t = t.squeeze()
    print('after flatten:',t)
    return



def main():
    print(torch.cuda.is_available())


    # x = torch.tensor((3,1,5,8))
    # print(x)


    # arr = np.ones((3,3))
    # print("数据类型为：",arr.dtype)
    # t = torch.tensor(arr)
    # print(t)
    # print(t.device)
    # print(t.layout)
    # print(t.dtype)


    # x = torch.tensor(([3,1,5,8],[2,6,9,8],[6,8,4,1]))
    # x = x.reshape((1,-1))
    # print(x)

    # t = torch.arange(15).reshape((3,5))
    # t1 = torch.arange(15).reshape((3,5))

    # t = t.reshape((1,15))
    # # t = t.reshape((1,-1))
    # print('正常的t是',t)
    # flatten(t1)


    t = torch.tensor([
        [1,8,9,2],
        [4,5,2,1],
        [5,6,8,1],
        [3,5,4,3]
    ])
    print(t<7)
    print(t.le(7))
    print(t.sum(dim=1))


if __name__ == "__main__":
    main()