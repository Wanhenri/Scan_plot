import glob
import csv
import pandas as pd
import matplotlib.pyplot as plt

def plot_ROC(var_1, var_2,var_3, title,time,statistic):
    path =r'data/dadosscantec/' # use your path
    allFiles = glob.glob(path + "/"+str(statistic)+"EXP"+ str(time) + "*.csv")

    list_ = []

    for file_ in allFiles:
        df = pd.read_csv(file_)
        list_.append(df)
        ts = df.loc[0:107,[var_1, var_2,var_3]]
        print(file_)
        plt.plot(ts)
        plt.title(title)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.legend([var_1, var_2,var_3], loc=0)
        plt.tight_layout()
        plt.plot()
        plt.savefig(str(title)+str(statistic)+str(time)+'.png')

#A 'def' abaixo é exclusiva para as váriaveis PSNM-000 e AGPL-925

def plot_ROC_1_var(var_1, title,time,statistic):
    path =r'data/dadosscantec/' # use your path
    allFiles = glob.glob(path + "/"+str(statistic)+"EXP"+ str(time) + "*.csv")

    list_ = []

    for file_ in allFiles:
        df = pd.read_csv(file_)
        list_.append(df)
        ts = df.loc[0:107,[var_1]]
        print(file_)
        plt.plot(ts)
        plt.title(title)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.legend([var_1], loc=0)
        plt.tight_layout()
        plt.plot()
        plt.savefig(str(title)+str(statistic)+str(time)+'.png')
        
plt.figure(figsize=(10,10))
plot_ROC_1_var('PSNM-000','PSNM','6','ACOR')

plt.figure(figsize=(10,10))
plot_ROC_1_var('AGPL-925','AGPL','6','ACOR')


# numero 6 - > relacionado a 24h
plt.figure(figsize=(15,15))

plt.subplot(6, 2, 1)
plot_ROC('VTMP-925','VTMP-850','VTMP-500','VTMP','6','ACOR')

plt.subplot(6, 2, 3)
plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','6','ACOR')

plt.subplot(6, 2, 5)
plot_ROC('UMES-500','UMES-850','UMES-925','UMES','6','ACOR')

plt.subplot(6,2,7)
plot_ROC('ZGEO-250','ZGEO-500','ZGEO-850','ZGEO','6','ACOR')

plt.subplot(6,2,9)
plot_ROC('UVEL-250','UVEL-500','UVEL-850','UVEL','6','ACOR')

plt.subplot(6,2,11)
plot_ROC('VVEL-250','VVEL-500','VVEL-850','VVEL','6','ACOR')

# numero 10 - > relacionado a 48h
plt.figure(figsize=(15,15))

plt.subplot(6, 2, 1)
plot_ROC('VTMP-925','VTMP-850','VTMP-500','VTMP','10','ACOR')

plt.subplot(6, 2, 3)
plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','10','ACOR')

plt.subplot(6, 2, 5)
plot_ROC('UMES-500','UMES-850','UMES-925','UMES','10','ACOR')

plt.subplot(6,2,7)
plot_ROC('ZGEO-250','ZGEO-500','ZGEO-850','ZGEO','10','ACOR')

plt.subplot(6,2,9)
plot_ROC('UVEL-250','UVEL-500','UVEL-850','UVEL','10','ACOR')

plt.subplot(6,2,11)
plot_ROC('VVEL-250','VVEL-500','VVEL-850','VVEL','10','ACOR')

# numero 14 - > relacionado a 72h
plt.figure(figsize=(15,15))

plt.subplot(6, 2, 1)
plot_ROC('VTMP-925','VTMP-850','VTMP-500','VTMP','14','ACOR')

plt.subplot(6, 2, 3)
plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','14','ACOR')

plt.subplot(6, 2, 5)
plot_ROC('UMES-500','UMES-850','UMES-925','UMES','14','ACOR')

plt.subplot(6,2,7)
plot_ROC('ZGEO-250','ZGEO-500','ZGEO-850','ZGEO','14','ACOR')

plt.subplot(6,2,9)
plot_ROC('UVEL-250','UVEL-500','UVEL-850','UVEL','14','ACOR')

plt.subplot(6,2,11)
plot_ROC('VVEL-250','VVEL-500','VVEL-850','VVEL','14','ACOR')

# numero 18 - > relacionado a 96h
plt.figure(figsize=(15,15))

plt.subplot(6, 2, 1)
plot_ROC('VTMP-925','VTMP-850','VTMP-500','VTMP','18','ACOR')

plt.subplot(6, 2, 3)
plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','18','ACOR')

plt.subplot(6, 2, 5)
plot_ROC('UMES-500','UMES-850','UMES-925','UMES','18','ACOR')

plt.subplot(6,2,7)
plot_ROC('ZGEO-250','ZGEO-500','ZGEO-850','ZGEO','18','ACOR')

plt.subplot(6,2,9)
plot_ROC('UVEL-250','UVEL-500','UVEL-850','UVEL','18','ACOR')

plt.subplot(6,2,11)
plot_ROC('VVEL-250','VVEL-500','VVEL-850','VVEL','18','ACOR')

# numero 22 - > relacionado a 120h
plt.figure(figsize=(15,15))

plt.subplot(6, 2, 1)
plot_ROC('VTMP-925','VTMP-850','VTMP-500','VTMP','22','ACOR')

plt.subplot(6, 2, 3)
plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','22','ACOR')

plt.subplot(6, 2, 5)
plot_ROC('UMES-500','UMES-850','UMES-925','UMES','22','ACOR')

plt.subplot(6,2,7)
plot_ROC('ZGEO-250','ZGEO-500','ZGEO-850','ZGEO','22','ACOR')

plt.subplot(6,2,9)
plot_ROC('UVEL-250','UVEL-500','UVEL-850','UVEL','22','ACOR')

plt.subplot(6,2,11)
plot_ROC('VVEL-250','VVEL-500','VVEL-850','VVEL','22','ACOR')

# numero 26 - > relacionado a 144h
plt.figure(figsize=(15,15))

plt.subplot(6, 2, 1)
plot_ROC('VTMP-925','VTMP-850','VTMP-500','VTMP','26','ACOR')

plt.subplot(6, 2, 3)
plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','26','ACOR')

plt.subplot(6, 2, 5)
plot_ROC('UMES-500','UMES-850','UMES-925','UMES','26','ACOR')

plt.subplot(6,2,7)
plot_ROC('ZGEO-250','ZGEO-500','ZGEO-850','ZGEO','26','ACOR')

plt.subplot(6,2,9)
plot_ROC('UVEL-250','UVEL-500','UVEL-850','UVEL','26','ACOR')

plt.subplot(6,2,11)
plot_ROC('VVEL-250','VVEL-500','VVEL-850','VVEL','26','ACOR')

# <><><><><><><><<><>

# numero 6 - > relacionado a 24h
plt.figure(figsize=(15,15))

plt.subplot(6, 2, 1)
plot_ROC('VTMP-925','VTMP-850','VTMP-500','VTMP','6','RMSE')

plt.subplot(6, 2, 3)
plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','6','RMSE')

plt.subplot(6, 2, 5)
plot_ROC('UMES-500','UMES-850','UMES-925','UMES','6','RMSE')

plt.subplot(6,2,7)
plot_ROC('ZGEO-250','ZGEO-500','ZGEO-850','ZGEO','6','RMSE')

plt.subplot(6,2,9)
plot_ROC('UVEL-250','UVEL-500','UVEL-850','UVEL','6','RMSE')

plt.subplot(6,2,11)
plot_ROC('VVEL-250','VVEL-500','VVEL-850','VVEL','6','RMSE')

# numero 10 - > relacionado a 48h
plt.figure(figsize=(15,15))

plt.subplot(6, 2, 1)
plot_ROC('VTMP-925','VTMP-850','VTMP-500','VTMP','10','RMSE')

plt.subplot(6, 2, 3)
plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','10','RMSE')

plt.subplot(6, 2, 5)
plot_ROC('UMES-500','UMES-850','UMES-925','UMES','10','RMSE')

plt.subplot(6,2,7)
plot_ROC('ZGEO-250','ZGEO-500','ZGEO-850','ZGEO','10','RMSE')

plt.subplot(6,2,9)
plot_ROC('UVEL-250','UVEL-500','UVEL-850','UVEL','10','RMSE')

plt.subplot(6,2,11)
plot_ROC('VVEL-250','VVEL-500','VVEL-850','VVEL','10','RMSE')
