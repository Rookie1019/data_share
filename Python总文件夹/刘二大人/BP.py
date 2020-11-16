import torch 


x_data = [1.0,2.0,3.0]
y_data = [2.0,4.0,6.0]

# ---------------------------------------------
# 相当于构建计算图
w = torch.Tensor([1.0])
w.requires_grad = True 

def forward(x):
    return x * w # w是一个tensor


def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y)**2
# ---------------------------------------------


def main():
    # print(w.grad.data)
      # 计算梯度
    for epoch in range(30):
        for x, y in zip(x_data, y_data):
            l = loss(x, y)   # 前馈过程
            l.backward()     # 反馈过程       每做一次反馈过程  计算图就会被释放  在下一次forward的时候再次创建
            print('grad 是 ',x, y, w.grad.item())
            w.data = w.data - 0.01 * w.grad.data

            w.grad.data.zero_()    # 必须把权重的梯度数据清零
        print('progress :',epoch,l.item())
    print('predict (after training): ',4,forward(4).item())


if __name__ == "__main__":
    main()
