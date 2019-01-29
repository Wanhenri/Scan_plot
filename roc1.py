import glob
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_ROC_1_var(var_1,title,time,statistic):
    path =r'dadosscantec/' # use your path
    allFiles = glob.glob(path + "/"+str(statistic)+"EXP"+ str(time) + "*.csv")

    list_ = []

    for file_ in allFiles:
        df = pd.read_csv(file_)
        list_.append(df)
        ts = df.loc[0:107,[var_1]]
        print(file_)
        plt.plot(ts)
        plt.title(title+'_'+str(statistic)+str(time))
        #plt.xlabel("X-axis")
        #plt.ylabel("Y-axis")
        plt.legend([var_1], loc=0)
        plt.tight_layout()
        plt.plot()
        plt.savefig('img/'+ str(title)+str(statistic)+str(time)+'.png')
        return