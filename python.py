import numpy as np
import pandas as pd 
import seaborn as sns
import string
from pylab import rcParams
import re
import math
import matplotlib.pyplot as plt
from matplotlib import rc
from sklearn.model_selection import train_test_split
from collections import Counter,defaultdict
from bs4 import BeautifulSoup
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
import nltk

sns.set(style='whitegrid', palette='muted', font_scale=1.5)
rcParams['figure.figsize']=8,4
RANDOM_SEED=42
np.random.seed(RANDOM_SEED)

data=pd.read_csv("data.xlsx")


f = sns.countplot(x='sentiment', data=data)
f.set_title("Sentiment distribution") 
f.set_xticklabels(['Negative', 'Positive']) 
plt.xlabel("");

