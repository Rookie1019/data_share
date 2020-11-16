import numpy as np
from numpy import *
import scipy.special

def sigmoid(x):
    return 1/(1+np.exp(-x))


def stock(data,classlabels):
    m,n = shape(data)
    alpha = 0.01
    weights = ones(n)
    for i in range(m):
        h = (sum(data[i]*weights))
        error = classlabels[i] - h
        weights = weights + alpha*error*data[i]
    return weights


weig = stock()


