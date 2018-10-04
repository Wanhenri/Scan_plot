#utilizado tambḿe no jupyter notebook
%matplotlib notebook

import glob
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path =r'data/dadosscantec/' # use your path
allFiles = glob.glob(path + "/ACOREXP*.csv")

frame = pd.DataFrame()
list_ = []

for file_ in allFiles:
    df = pd.read_csv(file_)
    list_.append(df)
    ts = df.loc[0:107,['VTMP-500']]
    print(file_)
    plt.plot(ts) 
