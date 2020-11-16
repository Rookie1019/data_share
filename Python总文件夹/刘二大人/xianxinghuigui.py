import numpy as np
import torch
import matplotlib as plt

learn_rate = 0.01




def main():
    # 1) 准备数据
    # y = 3*x + 0.8
    x = torch.rand([500,1])
    y_true = x*3 + 0.8
    
    # 2) 通过模型计算预测值
    w = torch.rand([1,1], requires_grad=True)
    b = torch.rand(0, requires_grad=True, dtype=torch.float32)
    

    # 3) 计算loss

    # 4) 通过循环计算参数
    for i in range(100):

        y_predict = torch.matmul(x, w) + b
        loss = (y_predict-y_true).pow(2).mean()


        if w.grad is not None:
            w.grad.data.zero_()
        if b.grad is not None:
            b.grad.data.zero_()
        
        loss.backward()
        w.data = w.data - learn_rate*w.data
        b.data = b.data - learn_rate*b.data
        print(loss.item())

















if __name__ == "__main__":
    main()