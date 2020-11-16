import torch
from torch.utils.data import DataLoader, Dataset  # dataset抽象类 只能被继承 不能创建对象
import pandas as pd 
import numpy as np
from torchtext.data import Field

# 构造数据集
# mini-batch  均衡性能和计算时间

class Data(Dataset):
    """
    数据集的类  通过init加载到内存中
    """
    def __init__(self, filepath):
        super().__init__()
        xy = pd.read_csv(filepath)
        xy = np.array(xy)

        self.len = xy.shape[0]
        self.x_data = torch.from_numpy(xy[:,:-1])
        self.y_data - torch.from_numpy(xy[:,[-1]])

    def __getitem__(self, index): # 这个方法可以确定对象可以根据索引取值
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len


class model_c(torch.nn.Module):
    """
    模型对象
    """
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 6)
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3 = torch.nn.Linear(4, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.sigmoid(self.linear1(x))
        x = self.sigmoid(self.linear2(x))
        x = self.sigmoid(self.linear3(x))
        return x



def main():

    model = model_c()
    creation = torch.nn.BCELoss(size_average=False)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    dataset = Data('路径')
    train_loader = DataLoader(dataset=dataset,
                            batch_size=32,   # 每个batch有多少个
                            shuffle=True,    # 是否打乱
                            num_workers=2)   # 进程个数
    # 训练过程
    for epoch in range(100):
        for i, data in enumerate(train_loader, 0):
            x_test, y_test = data

            y_pred = model(x_test)
            loss = creation(y_pred, y_test)
            print(epoch, loss.item())

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()


if __name__ == "__main__":
    main()