from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_20newsgroups



def nb_news():
    """
    用朴素贝叶斯算法对新闻进行分类
    :return:
    """
    # 1) 获取数据
    news = fetch_20newsgroups(subset='all')  # 注意几个参数都是什么意思
    
    # 2) 划分数据集
    x_train,x_test,y_train,y_test = train_test_split(news.data,news.target)
    # print(x_train)
    print(y_train)

    # 3) 特征工程 文本信息提取 Tfidf
    transfer = TfidfVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test) # https://blog.csdn.net/qq_28334183/article/details/88896111

    print(len(x_train))
    # 4) 朴素贝叶斯算法
    estimator = MultinomialNB()
    estimator.fit(x_train,y_train) 
    # 5) 模型评估
    # 方法1 : 直接对比真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict : ', y_predict)
    print('直接对比真实值和预测值 : ', y_test == y_predict)
    # 方法2 : 计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率是 : ', score)


if __name__ == "__main__":
    nb_news()