import nltk
from nltk.stem import WordNetLemmatizer



def download_nl():
    # nltk.set_proxy('SYSTEM PROXY')
    # nltk.download()
    wooo = WordNetLemmatizer()

    print(wooo.lemmatize('dogs'))

if __name__ == '__main__':
    download_nl()