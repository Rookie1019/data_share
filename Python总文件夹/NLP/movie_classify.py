import numpy as np
from keras import Sequential
from keras.datasets import imdb
from keras.layers import Dense, SimpleRNN, Embedding
from keras.preprocessing import sequence
from numpy.core.defchararray import mod


MAX_LEN = 500
MAX_FEATURES = 10000
BATCH_SIZE = 32



# def data2():
#     b = np.load(r'G:\nlp_data\imdb.npz',allow_pickle=True)
#     print(b.files)
#     print(b['x_train'])

# 准备数据
def data():


    # (input_train, y_train), (input_test, y_test) = imdb.load_data(num_words=MAX_FEATURES)
    b = np.load(r'G:\nlp_data\imdb.npz',allow_pickle=True)
    
    input_train = b['x_train']
    y_train = b['y_train']
    input_test = b['x_test']
    y_test = b['y_test']
    input_train = sequence.pad_sequences(input_train, maxlen=MAX_LEN)
    input_test = sequence.pad_sequences(input_test, maxlen=MAX_LEN)
    y = input_test.shape
    x = input_train.shape



    model = Sequential()
    model.add(Embedding(500, 32))
    model.add(SimpleRNN(32))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
    
    history = model.fit(input_train, input_test, epochs=128, batch_size=128, validation_split=0.2)
    print(history)

def main():




    data()



if __name__ == "__main__":
    main()