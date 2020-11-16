import torch

x_data = torch.tensor([[1.0],[2.0],[3.0]])
y_data = torch.tensor([[0],[0],[1]])

class Logistic_R(torch.nn.Module):
    def __init__(self):
        super(Logistic_R, self).__init__()
        self.linear = torch.nn.Linear(1, 1)     # 输入为1 输出为1 如果是(8,1)就是输入是8 输出是1
    
    def forward(self, x):
        y_pred = torch.sigmoid(self.linear(x))
        return y_pred



def main():
    model = Logistic_R()
    criterion = torch.nn.BCELoss(size_average=False)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    for epoch in range(100):
        y_pred = model(x_data)
        loss = criterion(y_pred, y_data)
        print(epoch, loss.item())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    print('w = ',model.linear.weight.item()) 
    print('b = ',model.linear.bias.item())
 

    x_test = torch.tensor([[6.0]])
    y_test = model(x_test)
    print('最后的预测值是: ',y_test)




if __name__ == "__main__":
    main()
