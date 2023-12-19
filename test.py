import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torchvision
import numpy as np
import pandas 
import matplotlib.pyplot as plt
import re
import os

import nltk
from nltk.tokenize import word_tokenize
from nltk import PorterStemmer
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords

from pymystem3 import Mystem


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split



data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]} 
a=np.array(data['Age'])
b=np.array([5,7,19,3])
print(type(a[0]))
x_train, y_train = train_test_split(b, a)
y_train = Variable(torch.from_numpy(y_train)).int()