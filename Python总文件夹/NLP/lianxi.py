from keras.layers import SimpleRNN, Embedding
from keras.models import Sequential
from gensim.corpora import WikiCorpus
import os
import seaborn as sns
import torch
import pandas as pd

data = pd.read_excel()


class lei(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.LSTM()