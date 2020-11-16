import pandas as pd
from math import log
import operator
"""
    1 收集数据
    2 准备数据 树构造算法只适用于标准型函数，因此数值型数据必须离散化
    3 分析数据 构造树完成之后，应该检查图形是否符合预期
    4 训练算法 构造树的数据结构
    5 测试算法 使用经验树计算错误率
    6 使用算法
    :return:
"""


# 第一步 计算信息熵的函数 3-1
def calcShannonEnt(dataset):
    numEntries = len(dataset)
    # print('dataset的len是 : ',numEntries)
    labelCounts = {}
    for featVec in dataset:
        currentlabel = featVec[-1]
        if currentlabel not in labelCounts.keys():
            labelCounts[currentlabel] = 0
        labelCounts[currentlabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob*log(prob,2)
    return shannonEnt

# 自己构建数据集的函数
def createDataset():
    dataset = [
        [1, 1,'yes'],
        [1, 1,'yes'],
        [1, 0,'no'],
        [0, 1,'no'],
        [0, 1,'no']
        # # 下面作为测试用的数据集
        # [1, 1, 1,'yes'],
        # [1, 1, 1,'yes'],
        # [0, 1, 1,'yes'],
        # [1, 0, 0,'no'],
        # [0, 1, 0,'no'],
        # [0, 1, 0,'no']
    ]
    labels = ['no surfaecing','flippers']
    return dataset,labels

# 降维或者是抽取特征的函数 按照给定的特征划分数据集 3-2
def splitDataset(dataset, axis, value):
    retDataset = []
    for featVec in dataset:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis+1:])
            retDataset.append(reduceFeatVec)
    return retDataset


# 选择最好的数据集划分方式  3-3
def chooseBestFeatureToSplit(dataset):
    numFeature = len(dataset[0])-1     # 特征个数
    print('len(dataset[0])-1 是 :',numFeature)
    baseEntropy = calcShannonEnt(dataset)      # 总的信息熵
    print('calcShannonEnt(dataset) 是 :',baseEntropy)
    bestinfoGain = 0.0
    bestFeature = -1
    for i in range(numFeature):
        featList = [example[i] for example in dataset]  # 这代码 看着头疼
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataset(dataset,i,value)
            prob = len(subDataSet)/float(len(dataset))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if infoGain > bestinfoGain:
            bestinfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

# 创建树的函数代码   3-4
def create_tree(dataset,labels):
    classList = [example[-1] for example in dataset]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataset[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataset)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataset]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = create_tree(splitDataset(
            dataset,bestFeat,value
        ),subLabels)
    return myTree


if __name__ == '__main__':
    mydata,mylabels = createDataset()
    # new_data = splitDataset(mydata,0,1)
    # print('mylabels: ',mylabels)
    # print(mydata)
    # ShannonEnt = calcShannonEnt(mydata)
    # print(ShannonEnt)
    # best = chooseBestFeatureToSplit(mydata)   # 0   意思就是选择第0个特征作为根节点
    # print(best)
    mytree = create_tree(mydata,mylabels)
    print(mytree)


