import torch
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

xy = np.loadtxt('csv文件.csv', delimiter=',', dtype=np.float32)
xy = pd.read_csv(r'C:\Users\Rookie\Desktop\csv文件.csv')
xy = np.array(xy)

x_data = torch.from_numpy(xy[:,:-1])
y_data = torch.from_numpy(xy[:,[-1]])   # 这里[-1]而不是-1 能保证输出的是矩阵
x_data = x_data.float()
y_data = y_data.float()

class multiply(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(5, 3)
        self.linear2 = torch.nn.Linear(3, 2)
        self.linear3 = torch.nn.Linear(2, 1)
        self.sigmiod = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.sigmiod(self.linear1(x))   # 这个x相当于第一层的输出 
        x = self.sigmiod(self.linear2(x))   # 这个x相当于第二层的输出 
        x = self.sigmiod(self.linear3(x))   # 这个x相当于第三层的输出
        return x


def main():
    # print(xy)
    # print('x_data: ',y_data)
    model = multiply()
    criterion = torch.nn.BCELoss(size_average=False)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    for epoch in range(100):
        y_pred = model(x_data)
        loss = criterion(y_pred, y_data)
        print(epoch, loss.item())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # print('w = ',model.linear.weight.item())
    # # print('b = ',model.linear.bias.item())

    x_test = np.array([0.1,0.9,0.2,0.32,0.2])
    x_test = torch.from_numpy(x_test)
    x_test = x_test.float()
    y_test = model(x_test)
    print('最后的预测值是: ',y_test)


if __name__ == "__main__":
    main()