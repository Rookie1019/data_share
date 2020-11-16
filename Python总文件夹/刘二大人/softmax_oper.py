import torch
from torchvision import datasets, transforms  # 对图像进行处理的东西
from torch.utils.data import DataLoader
import torch.optim as optim
import torch.nn.functional as F