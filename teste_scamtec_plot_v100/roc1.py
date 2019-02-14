import glob
import pandas as pd
import matplotlib.pyplot as plt
from time_exec import time_statistics

def peace_figure(ts,var_1,title,time,statistic,previsao):
        plt.plot(ts)
        plt.title(title+'_'+str(statistic)+str(time)+'_Prev_'+str(previsao)+'_horas')
        plt.xlabel("Tempo")
        plt.ylabel(str(statistic))
        plt.legend([var_1], loc=0)
        plt.tight_layout()
        plt.plot()
        return


@time_statistics
def plot_ROC_1_var(var_1,title,time,statistic,previsao):
    path =r'dadosscantec/' # use your path
    allFiles = glob.glob(path + "/"+str(statistic)+"EXP"+ str(time) + "*.csv")

    list_ = []

    for file_ in allFiles:
        df = pd.read_csv(file_)
        list_.append(df)
        ts = df.loc[0:107,[var_1]]
        print(file_)
        
        peace_figure(ts,var_1,title,time,statistic,previsao)
        
        plt.savefig('img/'+ str(title)+str(statistic)+str(time)+'.png')
        return
