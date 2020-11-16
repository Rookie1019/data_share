import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import f1_score


def ridge_regression():
    train_df = pd.read_csv(r'C:\Users\Rookie\Desktop\nlp\train_set.csv',sep='\t')
    
    
    vectorizer = CountVectorizer(max_features=3000)
    train_test = vectorizer.fit_transform(train_df['text'])

    clf = RidgeClassifier()
    clf.fit(train_test[:10000], train_df['label'].values[:10000])

    val_pred = clf.predict(train_test[10000:])
    print(f1_score(train_df['label'].values[10000:], val_pred, average='macro'))


def tfidf_ridge():
    
    train_df = pd.read_csv(r'C:\Users\Rookie\Desktop\nlp\train_set.csv',sep='\t')
    x_train = train_df['text']
    y_train = train_df['label']


    vectorizer = TfidfVectorizer(ngram_range=(1,3),max_features=3000)

    x_train = vectorizer.fit_transform(x_train)  # 转换成tfidf
    # print(x_train)

    clf = RidgeClassifier()
    clf.fit(x_train[:10000],y_train.values[:10000])

    y_pred = clf.predict(x_train[10000:])
    print(f1_score(y_train.values[10000:],y_pred=y_pred, average='macro'))

def ceshi():
    # import jieba
    # sentence = "我爱北京天安门"
    # seg_list = jieba.cut(sentence, cat_all=True)
    # print("Full Mode", "/".join(seg_list))  # 全模式
    # seg_list = jieba.cut(sentence, cat_all=False)
    # print("Full Mode", "/".join(seg_list))  # 精确模式
    # seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
    # print("Full Mode", "/".join(seg_list))
    # seg_list = jieba.cut_for_search("⼩小明硕⼠士毕业于中国科学院计算所，后在⽇日本东京大学深造")
    # # 搜索引擎模式
    # print(", ".join(seg_list))
    print('下载完成')
if __name__ == "__main__":


    # ridge_regression()

    # tfidf_ridge()

    ceshi()