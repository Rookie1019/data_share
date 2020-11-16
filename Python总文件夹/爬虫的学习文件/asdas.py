from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense
# import 
docs = ["The cat sat on the mat.", "I love green eggs and ham."]

# 只考虑最常见的8个单词
max_words = 8
# 统一的序列化长度
# 大于这个长度截断，小于这个长度用0补全
maxlen = 5
# 嵌入的维度
embedding_dim = 3

# 分词
tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(docs)
# 字典
word_index = tokenizer.word_index

# 序列化
sequences = tokenizer.texts_to_sequences(docs)
# 统一序列长度
data = pad_sequences(sequences, maxlen=maxlen)

# Embedding模型
model = Sequential()
# Embedding至少需要max_wrods和embedding_dim两个参数
model.add(Embedding(max_words, embedding_dim, input_length=maxlen, name='embedding'))
model.compile('rmsprop', 'mse')

out = model.predict(data)
print(out)
print(out.shape)
# 查看权重
layer = model.get_layer('embedding')
print(layer.get_weights())