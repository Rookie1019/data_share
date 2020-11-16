import torch
import torch.nn as nn
import torch.optim as optim
 
from torchtext.datasets import TranslationDataset, Multi30k
from torchtext.data import Field, BucketIterator
 
import spacy
import random
import math
import time
 
#1、preparing data
#设置一个随机种子
SEED = 1234
random.seed(SEED)
torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = True  #使用cuda保证每次结果一样。将这个 flag 置为True的话，每次返回的卷积算法将是确定的，即默认算法。如果配合上设置 Torch 的随机种子为固定值的话，应该可以保证每次运行网络的时候相同输入的输出是固定的
 
 
#创建tokenizer
spacy_de = spacy.load('de')
spacy_en = spacy.load('en')
 
 
 
#把tokenizer从一串字符转成一个list，同时做一个reverse取反
#在原论文中，作者发现颠倒源语言的输入的顺序可以取得不错的翻译效果，例如，一句话为“good morning!”，颠倒顺序分词后变为"!", “morning”, 和"good"。
 
#将德语进行分词并颠倒顺序
def tokenize_de(text):
    return [tok.text for tok in spacy_de.tokenizer(text)][::-1]
#将英语进行分词，不颠倒顺序
def tokenize_en(text):
    return [tok.text for tok in spacy_en.tokenizer(text)]
 
 
#我们创建SRC和TRG两个Field对象，tokenize为我们刚才定义的分词器函数，在每句话的开头加入字符SOS，结尾加入字符EOS，将所有单词转换为小写。
 
#TorchText的Field定义数据应该如何被处理
#SRC即source，是德语
#TRG即target，是英语
#sos是start of sequence, eos是end of sequence
#lower=True是将所有单词转换为小写
SRC = Field(tokenize = tokenize_de,
            init_token = '<sos>',
            eos_token = '<eos>',
            lower = True)
 
TRG = Field(tokenize = tokenize_en,
            init_token = '<sos>',
            eos_token = '<eos>',
            lower = True)
 
 
#使用torchtext自带的Multi30k数据集，这是一个包含约30000个平行的英语、德语和法语句子的数据集，每个句子包含约12个单词。
train_data, valid_data, test_data = Multi30k.splits(exts = ('.de', '.en'),
                                                    fields = (SRC, TRG))
 
#查看一下加载完的数据集
print(f"Number of training examples: {len(train_data.examples)}")
print(f"Number of validation examples: {len(valid_data.examples)}")
print(f"Number of testing examples: {len(test_data.examples)}")
 
 
#看一下生成的第一个训练样本，可以看到源语言的顺序已经颠倒了
print(vars(train_data.examples[0]))
 
 
#构建词表
#所谓构建词表，即需要给每个单词编码，也就是用数字表示每个单词，这样才能传入模型。
#可以使用dataset类中的build_vocab()方法传入用于构建词表的数据集。
#注意，源语言和目标语言的词表是不同的，而且词表应该只从训练集构建，而不是验证/测试集，这可以防止“信息泄漏”到模型中。
SRC.build_vocab(train_data, min_freq = 2) #设置最小词频为2，当一个单词在数据集中出现次数小于2时会被转换为<unk>字符。
TRG.build_vocab(train_data, min_freq = 2)
 
 
#查看一下生成的词表大小
print(f"Unique tokens in source (de) vocabulary: {len(SRC.vocab)}")
print(f"Unique tokens in target (en) vocabulary: {len(TRG.vocab)}")
 
 
#指定GPU还是CPU进行训练
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
 
 
 
 
BATCH_SIZE = 128
 
#创建迭代器
train_iterator, valid_iterator, test_iterator = BucketIterator.splits(
    (train_data, valid_data, test_data),
    batch_size = BATCH_SIZE,
    device = device)
 
#查看一下生成的batch
batch = next(iter(train_iterator))
print(batch)
#输出:
# [torchtext.data.batch.Batch of size 128 from MULTI30K]
# 	[.src]:[torch.cuda.LongTensor of size 23x128 (GPU 0)]
# 	[.trg]:[torch.cuda.LongTensor of size 21x128 (GPU 0)]
 
 
 
#2、创建Seq2Seq模型
 
#我们将分别创建编码器（Encoder）、解码器（Eecoder）和seq2seq模型。
#原论文使用了一个4层的单向LSTM，出于训练时间的考虑，我们将其缩减到了2层。结构如图所示
 
class Encoder(nn.Module):
    def __init__(self, input_dim, emb_dim, hid_dim, n_layers, dropout):
        super().__init__()
 
        self.input_dim = input_dim
        self.emb_dim = emb_dim
        self.hid_dim = hid_dim
        self.n_layers = n_layers
        self.dropout = dropout
 
        self.embedding = nn.Embedding(input_dim, emb_dim)
 
        #encoder部分
        self.rnn = nn.LSTM(emb_dim, hid_dim, n_layers, dropout=dropout)
 
        self.dropout = nn.Dropout(dropout)
 
    def forward(self, src):
        #src:(sent_len, batch_size)
 
        embedded = self.dropout(self.embedding(src))
 
        #embedded:(sent_len, batch_size, emb_dim)
        outputs, (hidden, cell) = self.rnn(embedded)
        #outputs:(sent_len, batch_size, hid_dim)
        #hidden:(n_layers, batch_size, hid_dim)
        #cell:(n_layers, batch_size, hid_dim)
        return hidden, cell
 
 
class Decoder(nn.Module):
    def __init__(self, output_dim, emb_dim, hid_dim, n_layers, dropout):
        super().__init__()
 
        self.output_dim = output_dim
        self.emb_dim = emb_dim
        self.hid_dim = hid_dim
        self.n_layers = n_layers
        self.dropout = dropout
 
        self.embedding = nn.Embedding(output_dim, emb_dim)
 
        self.rnn = nn.LSTM(emb_dim, hid_dim, n_layers, dropout=dropout)
 
        self.out = nn.Linear(hid_dim, output_dim)
 
        self.dropout = nn.Dropout(dropout)
 
    def forward(self, input, hidden, cell):
        # input: (batch_size) -> input: (1, batch_size)
        input = input.unsqueeze(0)
        # embedded: (1, batch_size, emb_dim)
        embedded = self.dropout(self.embedding(input))
        # hidden: (n_layers, batch size, hid_dim)
        # cell: (n_layers, batch size, hid_dim)
        # output(1, batch_size, hid_dim)
        output, (hidden, cell) = self.rnn(embedded, (hidden, cell))
        # prediction: (batch_size, output_dim)
        prediction = self.out(output.squeeze(0))
 
        return prediction, hidden, cell
 
 
class Seq2Seq(nn.Module):
    def __init__(self, encoder, decoder, device):
        super().__init__()
 
        self.encoder = encoder
        self.decoder = decoder
        self.device = device
 
        assert encoder.hid_dim == decoder.hid_dim, \
            "Hidden dimensions of encoder and decoder must be equal!"
        assert encoder.n_layers == decoder.n_layers, \
            "Encoder and decoder must have equal number of layers!"
 
    def forward(self, src, trg, teacher_forcing_ratio=0.5):
        # src = [src sent len, batch size]
        # trg = [trg sent len, batch size]
        # teacher_forcing_ratio is probability to use teacher forcing
        # e.g. if teacher_forcing_ratio is 0.75 we use ground-truth inputs 75% of the time
 
        batch_size = trg.shape[1]
        max_len = trg.shape[0]
        trg_vocab_size = self.decoder.output_dim
 
        # tensor to store decoder outputs
        #创建outputs张量存储Decoder的输出
        outputs = torch.zeros(max_len, batch_size, trg_vocab_size).to(self.device)
 
        # last hidden state of the encoder is used as the initial hidden state of the decoder
        hidden, cell = self.encoder(src)
 
        #输入到Decoder网络的第一个字符是<sos>（句子开始标记）
        input = trg[0, :]
 
        for t in range(1, max_len):
            # insert input token embedding, previous hidden and previous cell states
            # receive output tensor (predictions) and new hidden and cell states
            output, hidden, cell = self.decoder(input, hidden, cell)
 
            # place predictions in a tensor holding predictions for each token
            outputs[t] = output
 
            # decide if we are going to use teacher forcing or not
            teacher_force = random.random() < teacher_forcing_ratio
 
            # get the highest predicted token from our predictions
            top1 = output.argmax(1)
 
            # if teacher forcing, use actual next token as next input
            # if not, use predicted token
            input = trg[t] if teacher_force else top1
 
        return outputs
 
 
#3、训练模型
 
#定义模型参数
INPUT_DIM = len(SRC.vocab)
OUTPUT_DIM = len(TRG.vocab)
ENC_EMB_DIM = 256
DEC_EMB_DIM = 256
HID_DIM = 512
N_LAYERS = 2
ENC_DROPOUT = 0.5
DEC_DROPOUT = 0.5
 
 
#编码器和解码器的嵌入层维度（emb_dim）和dropout可以不同，但是层数和隐藏层维度必须相同。
enc = Encoder(INPUT_DIM, ENC_EMB_DIM, HID_DIM, N_LAYERS, ENC_DROPOUT)  #7855 256 512 2 0.5
dec = Decoder(OUTPUT_DIM, DEC_EMB_DIM, HID_DIM, N_LAYERS, DEC_DROPOUT) #5893 256 512 2 0.5
 
model = Seq2Seq(enc, dec, device).to(device)
 
#初始化模型参数
#在原论文中，作者将所有参数初始化为-0.08和+0.08之间的均匀分布。我们通过创建一个函数来初始化模型中的参数权重。当使用apply方法时，模型中的每个模块和子模块都会调用init_weights函数。
def init_weights(m):
    for name, param in m.named_parameters():
        nn.init.uniform_(param.data, -0.08, 0.08)
 
model.apply(init_weights)
 
#看一下模型中可训练参数的总数量
def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)
 
print(f'The model has {count_parameters(model):,} trainable parameters')
 
 
 
#使用Adam作为优化器
optimizer = optim.Adam(model.parameters())
 
 
#使用交叉熵损失作为损失函数
#使用交叉熵损失作为损失函数，由于Pytorch在计算交叉熵损失时在一个batch内求平均，因此需要忽略target为的值（在数据处理阶段，一个batch里的所有句子都padding到了相同的长度，不足的用补齐），否则将影响梯度的计算
PAD_IDX = TRG.vocab.stoi['<pad>']
 
criterion = nn.CrossEntropyLoss(ignore_index = PAD_IDX)
 
 
#定义训练函数
def train(model, iterator, optimizer, criterion, clip):   #criterion是损失函数
    model.train()
 
    epoch_loss = 0
 
    for i, batch in enumerate(iterator):
        #这里的src和trg都是tensor的形式了
        src = batch.src
        trg = batch.trg
 
        optimizer.zero_grad()
 
        output = model(src, trg)
 
        # trg = [trg sent len, batch size]
        # output = [trg sent len, batch size, output dim]
 
        output = output[1:].view(-1, output.shape[-1])
        trg = trg[1:].view(-1)
 
        # trg = [(trg sent len - 1) * batch size]
        # output = [(trg sent len - 1) * batch size, output dim]
 
        loss = criterion(output, trg)
 
        loss.backward()
 
        torch.nn.utils.clip_grad_norm_(model.parameters(), clip)
 
        optimizer.step()
 
        epoch_loss += loss.item()
 
    return epoch_loss / len(iterator)
 
#定义验证函数，即val的
#评估阶段和训练阶段的区别是不需要更新任何参数
def evaluate(model, iterator, criterion):
    model.eval()
 
    epoch_loss = 0
 
    with torch.no_grad():
        for i, batch in enumerate(iterator):
            src = batch.src
            trg = batch.trg
 
            output = model(src, trg, 0)  # turn off teacher forcing
 
            # trg = [trg sent len, batch size]
            # output = [trg sent len, batch size, output dim]
 
            output = output[1:].view(-1, output.shape[-1])
            trg = trg[1:].view(-1)
 
            # trg = [(trg sent len - 1) * batch size]
            # output = [(trg sent len - 1) * batch size, output dim]
 
            loss = criterion(output, trg)
 
            epoch_loss += loss.item()
 
    return epoch_loss / len(iterator)
 
 
def epoch_time(start_time, end_time):
    elapsed_time = end_time - start_time
    elapsed_mins = int(elapsed_time / 60)
    elapsed_secs = int(elapsed_time - (elapsed_mins * 60))
    return elapsed_mins, elapsed_secs
 
 
#训练模型
N_EPOCHS = 10
CLIP = 1
 
best_valid_loss = float('inf')
 
for epoch in range(N_EPOCHS):
 
    start_time = time.time()
 
    train_loss = train(model, train_iterator, optimizer, criterion, CLIP)
    valid_loss = evaluate(model, valid_iterator, criterion)
 
    end_time = time.time()
 
    epoch_mins, epoch_secs = epoch_time(start_time, end_time)
 
    if valid_loss < best_valid_loss:
        best_valid_loss = valid_loss
        torch.save(model.state_dict(), 'tut1-model.pt')   #保存最佳验证损失的epoch参数作为模型的最终参数
 
    print(f'Epoch: {epoch + 1:02} | Time: {epoch_mins}m {epoch_secs}s')
    print(f'\tTrain Loss: {train_loss:.3f} | Train PPL: {math.exp(train_loss):7.3f}')
    print(f'\t Val. Loss: {valid_loss:.3f} |  Val. PPL: {math.exp(valid_loss):7.3f}')
    #math.exp()：使用一个batch内的平均损失计算困惑度
 
#4、验证模型
model.load_state_dict(torch.load('tut1-model.pt'))
 
test_loss = evaluate(model, test_iterator, criterion)
 
print(f'| Test Loss: {test_loss:.3f} | Test PPL: {math.exp(test_loss):7.3f} |')