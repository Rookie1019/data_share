import jieba
# import tensorflow
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from keras.layers import Embedding, GlobalAveragePooling1D, Dense
from keras.models import Sequential
from keras.preprocessing.text import Tokenizer
from keras.datasets import imdb

word_dic = ['我','爱','北京','天安门','北京天安门']

def cut_word():

    # x = "我来到上海图书馆借书，借到了五本书"
    # seg_list = jieba.cut(x)
    # print(type(seg_list))
    # for i in seg_list:
    #     print(i)

    # 小明硕士毕业于中国科学院计算所，后在日本京都大学深造
    jieba.add_word('意见')
    seg_list = jieba.cut("我们经常有意见分歧")  # 搜索引擎模式
    print(", ".join(seg_list))
    



def segment():
    """
    考虑语义
    
    """
    word_prob = {
        "北京":0.3,"的":0.08,"天":0.005,"气":0.005,"天气":0.06,"真":0.04,"好":0.05,"真好":0.04,"啊":0.01,"真好啊":0.02,
        "今":0.01,"今天":0.07,"课程":0.06,"内容":0.06,"有":0.05,"很":0.03,"很有":0.04,"意思":0.06,"有意思":0.005,"课":0.01,
        "程":0.005,"经常":0.08,"意见":0.08,"意":0.01,"见":0.005,"有意见":0.02,"分歧":0.04,"分":0.02,"歧":0.005
    }
    
    print(sum(word_prob.values()))

# 前向最大匹配
def forward():
    # print(word)

    max_len = 5
    input_word = '我爱北京天安门'

    set_list = []
    i = 0
    while i < max_len:
        for pos in reversed(range(max_len)):
            print('judge ',input_word[i:pos+i+1])
            if input_word[i:pos+i+1] in word_dic:
                set_list.append(input_word[i:pos+i+1])
                i = pos + i
                break
        i = i + 1
    print(set_list)


# 后向最大匹配
def back():

    max_len = 5
    input_word = '我爱北京天安门'

    set_list = []
    
    # print(input_word[-max_len:])
    i = len(input_word)
    while i > 0:
        for pos in reversed(range(max_len)):
            if i >= pos + 1:   # 这个判断忘记加
            
                print('judge ',input_word[i-pos-1:i])
                if input_word[i-pos-1:i] in word_dic:
                    set_list.append(input_word[i-pos-1:i])
                    i = i - pos
                    break
        i = i - 1
    print('/'.join(reversed(set_list)))



def vebitor():



    return

def hanshu():
    
    x = np.array([False,True,False,False,True])
    print(x)
    y = x.astype(np.int)
    print("y : ",y)
    return



if __name__ == "__main__":
    # cut_word()
    forward()
    
    # back()
    # hanshu()
    
    