from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def pca_demo():
    transfer = PCA(n_components=17)
    data = pd.read_excel(r'C:\Users\Rookie\Desktop\2020年中国研究生数学建模竞赛赛题\2020年B题\2020年B题--汽油辛烷值建模\数模题\附件一：325个样本数据处理版(1).xlsx',header=[1,2],index_col=0)

    data_new = data.drop(columns=[data.columns[0], data.columns[2], data.columns[10]]).copy()
    print(data_new.shape)
    data_new = transfer.fit_transform(data_new)
    print(data_new)
    # plt.figure(figsize=(12, 8))
    #
    # plt.title('Factor Analysis Components')
    #
    # plt.plot(data_new[:, 0], data_new[:, 1])
    #
    # plt.plot(data_new[:, 1], data_new[:, 2])
    #
    # plt.plot(data_new[:, 2], data_new[:, 0])
    # plt.show()

    return

if __name__ == '__main__':
    pca_demo()