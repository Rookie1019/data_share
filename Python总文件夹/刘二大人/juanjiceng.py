import torch

def main():
    input_layer = [
        3,4,5,6,7,
        2,4,6,8,2,
        1,6,7,8,4,
        9,7,4,6,2,
        3,7,5,4,1
    ]
    input_layer = torch.tensor(input_layer).view(1,1,5,5)   # view = reshape   B,n,w,h   Batch  小批量
    conv_layer = torch.nn.Conv2d(1,1,kernel_size=3,padding=1,bias=False)  # 卷积层

    kernel = torch.tensor([1,2,3,4,5,6,7,8,9]).view(1,1,3,3)  # 卷积核   o i w h  输出通道数 输入通道数
    conv_layer.weight.data = kernel.data

    output = conv_layer(input_layer)

    print(output)


if __name__ == "__main__":
    main()