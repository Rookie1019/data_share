import argparse
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


class SVMScrach():
    def __init__(self, nepoch, C, kernel, degree, coef0, epsilon):
        self.C = C
        self.nepoch = nepoch
        self.kernel = kernel
        self.degree = degree
        self.coef0 = coef0
        self.epsilon = epsilon

    def fit(self, X, y):
        """模型训练"""

    def predict(self, x):
        """模型训练"""

    def smo_inner(self, i, y):
        """smo内层循环"""
        if   # 如果外层循环违反KKT条件 我们才再内层循环中寻找第二个变量
    def violateKKT(self, i, y):
        """违反KKT条件的值"""
        if self.alpha[i] > 0 and self.alpha[i] < self.C:
            return abs(y[i] * self.g(i,y) - 1) < self.epsilon  # 绝对值小于给定的epsilon 就是违反的
        return True # 对于非间隔边界上面的样本 我们默认他是违反的

    def calc_E(self, i, y):
        return self.g(i, y) - y[i]

    def g(self, i, y):
        """alphah和y做内积，然后再乘以kernel函数，再加上b 就等于g(x) 也就是模型的预测"""
        return np.dot(self.alpha * y, self.K[i]) + self.b

    def smo_outer(self, y):
        """smo外层循环"""
        num_epoch = 0  # 记录迭代次数
        traverse_trainset = True  # 标识是否遍历整个训练集
        alpha_change = 0  # 标识alpha是否已经进行了更新
        while alpha_change > 0 or traverse_trainset:  # 只要进行了更新 我们就要继续循环
            alpha_change = 0
            if traverse_trainset:
                return

            else:
                # 这句话的意思是 我们要取到所有alpha大于0小于C的值的索引
                bound_sv_index = np.nonzero(np.logical_and(self.alpha > 0, self.alpha < self.C))[0]
                # 遍历边界上面的支持向量
                for i in range(bound_sv_index):
                    alpha_change += self.smo_inner(i, y)
            num_epoch += 1
            if num_epoch > self.nepoch:  # 如果达到了给定的nepoch数目 我们就退出循环
                break

            if traverse_trainset:
                traverse_trainset = False
            elif alpha_change == 0:
                # 如果没有找到合适的alpha 我们就要遍历整个训练集
                traverse_trainset = True

    # 48分钟的时候讲解参数
    def init_params(self, X, y):
        """初始化参数"""
        self.m = X.shape[0]  # 样本的个数
        self.n = y.shape[1]  # 维度
        self.alpha = np.zeros(self.m)
        self.b = 0

        self.ecache = np.zeros((self.m, 2))
        self.K = np.zeros((self.m, self.m))
        # 将输入空间中的X 转换为kernel矩阵   映射到kernel特征空间
        for i in range(self.m):
            for j in range(self.m):
                self.K[i, j] = self.kernel_transform(X[i], X[j])

    def kernel_transform(self, x1, x2):
        """选择核函数类型"""
        gamma = 1 / self.n  # gramma默认为维度分之一
        if self.kernel == 'linner':  # 线性核
            return np.dot(x1, x2)
        elif self.kernel == 'ploy':  # 多项式核
            return np.power(gamma * np.dot(x1, x2) + self.coef0, self.degree)
        else:                        # 高斯核
            return np.exp(-gamma * np.dot(x1 - x2, x1 - x2))


def main():
    # 参数准备
    parser = argparse.ArgumentParser(description='SVM算法实现的命令行参数')
    parser.add_argument('--nepoch', type=int, default=3000, help='训练多少个epoch后终止训练')
    parser.add_argument('--C', type=float, default=1, help='正则化系数')
    parser.add_argument('--kernel', type=str, default='rbf', help='核函数类型')
    parser.add_argument('--degree', type=int, default=3, help='多项式核函数次数')
    parser.add_argument('--coef0', type=float, default=0, help='多项式核函数中系数')
    parser.add_argument('--epsilon', type=float, default=0.001, help='检测第一个变量对应的样本是''否违反KKT条件的检验范围')
    args = parser.parse_args()

    X, y = load_iris(return_X_y=True)  # X是数据集 y是结果集
    y[:50] = -1
    print(y)
    x_train, x_test, y_train, y_test = train_test_split(X[:100], y[:100], train_size=0.8, shuffle=True)
    model = SVMScrach(args.nepoch, args.lr, args.loss_tolrance)

    n_test = x_test.shape[0]
    n_right = 0

    for i in range(n_test):
        y_pred = model.predict()  # 34

    return


if __name__ == '__main__':
    main()
