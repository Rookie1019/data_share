import numpy as np


def load_dataset():
    postingList = [
        ['my', 'dog', 'has', 'flea', 'problem', 'help', 'please'],
        ['maybe', 'not', 'him', 'to', 'dog', 'park', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
        ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
    ]
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec


def createVocabList(dataset):
    """
    相当于jieba分词工具  将矩阵的东西 转化到一维的数组中
    :param dataset: 矩阵
    :return: 返回一维数组 将所有元素转换到一维数组里面
    """
    vocabSet = set([])
    for document in dataset:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def setofWords2Vec(vocabList, inputSet):
    """
    :param vocabList:  这是一个一维数组 且没有重复的东西 (伯努利) 检查第二个参数是否在这个参数里面对应
    :param inputSet:  小的一维数组（词表） 检查这个词表里面的词是否出现国
    :return:  返回的是一维向量 且只有0 1 代表着第二个参数的元素是否在第一个里面出现
    """
    returnVec = [0] * len(vocabList)
    for word in inputSet:  # 遍历每个词条
        if word in vocabList:  # 如果在这里面
            returnVec[vocabList.index(word)] = 1  # 将数字变成1
        else:
            print('{}这个单词不在词表中'.format(word))
    return returnVec


def trainNBo(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainMatrix) / float(numTrainDocs)  # 侮辱性词语

    p0Num = np.zeros(numWords)
    p1Num = np.zeros(numWords)
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
    p1Vect = np.log(p1Num / p1Denom)  # 这里取对数是为了防止数字过小
    p0Vect = np.log(p0Num / p0Denom)  # python自动解释成0 比如0.00000007
    return p1Vect, p0Vect, pAbusive



def main():
    a, b = load_dataset()
    print(a[0])
    c = createVocabList(a)
    print(len(c))
    d = setofWords2Vec(c, a[0])
    print(d, len(d))


if __name__ == '__main__':
    main()
