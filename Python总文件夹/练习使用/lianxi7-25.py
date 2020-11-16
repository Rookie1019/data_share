import numpy as np
import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np


# x = np.arange(24).reshape((2,3,4))
# print(x)



# print(x.transpose((1,2,0)))


# print(torch.cuda.is_available())

# t = torch.tensor([5,6,9])
# t = t.cuda
# print(t)




def main():

    arr = np.arange(16).reshape((2,2,4))
    print(arr)

    arr = arr.transpose((0,2,1))
    print('转置后的矩阵为 \n',arr)


def con():
    
    a = np.arange(8).reshape(2,2,2)
    print('a',a)
    print(np.shape(a))
    b = np.arange(8).reshape(2,2,2)
    print('b',b)
    print(np.shape(b))
    c=np.concatenate((a, b), axis=0)  # axis=0是行，axis=1是列，缺省是行
    print('c',c)
    print(np.shape(c))
    print(len(c))
    d=np.concatenate((a, b), axis=1)
    print('d',d)
    print(np.shape(d))
    print(len(d))
    f=np.concatenate((a, b))
    print('f',f)
    print(np.shape(f))
    print(len(f))

def coocc():
    from gensim.models import Word2Vec

    en_wiki_word2vec_model = Word2Vec.load('wiki_zh_jian_text.model')

    testwords = ['金融','上','股票','跌','经济']
    for i in range(5):
        res = en_wiki_word2vec_model.most_similar(testwords[i])
        print (testwords[i])
        print (res)
    

if __name__ == "__main__":
    # main()
    # con()
    coocc()