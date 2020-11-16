import torch 
import torchvision

# srt = torchvision.datasets.MNIST()

# pytorch构建线性回归
# x_data = np.array([[1.0],[2.0],[3.0]])
# y_data = np.array([[2.0],[4.0],[6.0]])

x_data = torch.tensor([[1.0],[2.0],[3.0]])   # 构建张量
y_data = torch.tensor([[2.0],[4.0],[6.0]])

class LinearModel(torch.nn.Module):   # module会自动帮你实现反向过程 所以不需要自己实现bp
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1,1)   # Linear是一个类 里面包含了 权重和偏置 linear是一个对象

    
    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred


model = LinearModel()
criterion = torch.nn.MSELoss(size_average=False)   # 参数是否求均值 reduce看是否降维
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # parameters 会将所有需要优化的都放进去  lr学习率


# 相当于训练过程
for epoch in range(200):
    y_pred = model(x_data)    # 1. 算出y的预测值
    loss = criterion(y_pred, y_data)  # 2. y_pred - y 算出loss
    # print('y_pred : ', y_pred)
    # print('loss : ', loss)
    

    optimizer.zero_grad()     # 3. 梯度清零
    loss.backward()           # 4. 反向传播
    optimizer.step()          # 5. 更新梯度


# 测试过程

print('w = ',model.linear.weight.item())
print('b = ',model.linear.bias.item())


x_test = torch.tensor([[6.0],[4.0]])
y_test = model(x_test)
print('最后的预测值是: ',y_test)







