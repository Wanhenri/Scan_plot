import glob
import pandas as pd
import matplotlib.pyplot as plt

#function created

from roc1 import plot_ROC_1_var
from roc2 import plot_ROC
from fjso import select
from time_exec import time_statistics

# Checando as versões para acompanhamento de atualizações
print()
print("pandas version: {}". format(pd.__version__))
print()

a =select(6,3,8,4)


for b, c in zip(range(6,9,2), range(7,10,2)):
    for d, e in itertools.product(range(0,6), range(0,3)):
        plt.figure(figsize=(10,10))
        plot_ROC_1_var(str(a[3][b]),str(a[3][c]), a[0][d],a[2][e])
        
        print('Funcao: plot_ROC_1_var')
        print('Média de tempo [s]: ', sum(plot_ROC_1_var.times) / len(plot_ROC_1_var.times))


print("250 - 850")
for b, c in zip(range(0,4), range(0,4)):
  for e, f in itertools.product(range(0,6), range(0,3)):
        plt.figure(figsize=(10,10))
        plot_ROC(
                 str(a[3][b]) +'-'+ str(a[4][0]),
                 str(a[3][b]) +'-'+ str(a[4][1]),
                 str(a[3][b]) +'-'+ str(a[4][2]),
                 str(a[3][c]), a[0][e],a[2][f]
                 )

        print('Funcao: plot_ROC')
        print('Média de tempo [s]: ', sum(plot_ROC.times) / len(plot_ROC.times))


print("500-925")
for b, c in zip(range(4,6), range(4,6)):
  for e, f in itertools.product(range(0,6), range(0,3)):
        plt.figure(figsize=(10,10))
        plot_ROC(
                 str(a[3][b]) +'-'+ str(a[4][0]),
                 str(a[3][b]) +'-'+ str(a[4][1]),
                 str(a[3][b]) +'-'+ str(a[4][2]),
                 str(a[3][c]), a[0][e],a[2][f]
                 )

        print('Funcao: plot_ROC')
        print('Média de tempo [s]: ', sum(plot_ROC.times) / len(plot_ROC.times))






