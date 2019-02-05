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






####################

## numero 6 - > relacionado a 24h
#plt.figure(figsize=(15,15))
#
##plt.subplot(6, 2, 1)
#plot_ROC('VTMP-925','VTMP-850','VTMP-500','VTMP','6','ACOR')
##
##plt.subplot(6, 2, 3)
#plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','6','ACOR')
##
##plt.subplot(6, 2, 5)
#plot_ROC('UMES-500','UMES-850','UMES-925','UMES','6','ACOR')
##
##plt.subplot(6,2,7)
#plot_ROC('ZGEO-250','ZGEO-500','ZGEO-850','ZGEO','6','ACOR')
##
##plt.subplot(6,2,9)
#plot_ROC('UVEL-250','UVEL-500','UVEL-850','UVEL','6','ACOR')
#
##plt.subplot(6,2,11)
#plot_ROC('VVEL-250','VVEL-500','VVEL-850','VVEL','6','ACOR')

## numero 10 - > relacionado a 48h
#plt.figure(figsize=(15,15))
#
#plt.subplot(6, 2, 1)
#plot_ROC('VTMP-925','VTMP-850','VTMP-500','VTMP','10','ACOR')
#
#plt.subplot(6, 2, 3)
#plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','10','ACOR')
#
#plt.subplot(6, 2, 5)
#plot_ROC('UMES-500','UMES-850','UMES-925','UMES','10','ACOR')
#
#plt.subplot(6,2,7)
#plot_ROC('ZGEO-250','ZGEO-500','ZGEO-850','ZGEO','10','ACOR')
#
#plt.subplot(6,2,9)
#plot_ROC('UVEL-250','UVEL-500','UVEL-850','UVEL','10','ACOR')
#
#plt.subplot(6,2,11)
#plot_ROC('VVEL-250','VVEL-500','VVEL-850','VVEL','10','ACOR')
#
## numero 14 - > relacionado a 72h
#plt.figure(figsize=(15,15))
#
#plt.subplot(6, 2, 1)
#plot_ROC('VTMP-925','VTMP-850','VTMP-500','VTMP','14','ACOR')
#
#plt.subplot(6, 2, 3)
#plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','14','ACOR')
#
#plt.subplot(6, 2, 5)
#plot_ROC('UMES-500','UMES-850','UMES-925','UMES','14','ACOR')
#
#plt.subplot(6,2,7)
#plot_ROC('ZGEO-250','ZGEO-500','ZGEO-850','ZGEO','14','ACOR')
#
#plt.subplot(6,2,9)
#plot_ROC('UVEL-250','UVEL-500','UVEL-850','UVEL','14','ACOR')
#
#plt.subplot(6,2,11)
#plot_ROC('VVEL-250','VVEL-500','VVEL-850','VVEL','14','ACOR')
#
## numero 18 - > relacionado a 96h
#plt.figure(figsize=(15,15))
#
#plt.subplot(6, 2, 1)
#plot_ROC('VTMP-925','VTMP-850','VTMP-500','VTMP','18','ACOR')
#
#plt.subplot(6, 2, 3)
#plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','18','ACOR')
#
#plt.subplot(6, 2, 5)
#plot_ROC('UMES-500','UMES-850','UMES-925','UMES','18','ACOR')
#
#plt.subplot(6,2,7)
#plot_ROC('ZGEO-250','ZGEO-500','ZGEO-850','ZGEO','18','ACOR')
#
#plt.subplot(6,2,9)
#plot_ROC('UVEL-250','UVEL-500','UVEL-850','UVEL','18','ACOR')
#
#plt.subplot(6,2,11)
#plot_ROC('VVEL-250','VVEL-500','VVEL-850','VVEL','18','ACOR')
#
## numero 22 - > relacionado a 120h
#plt.figure(figsize=(15,15))
#
#plt.subplot(6, 2, 1)
#plot_ROC('VTMP-925','VTMP-850','VTMP-500','VTMP','22','ACOR')
#
#plt.subplot(6, 2, 3)
#plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','22','ACOR')
#
#plt.subplot(6, 2, 5)
#plot_ROC('UMES-500','UMES-850','UMES-925','UMES','22','ACOR')
#
#plt.subplot(6,2,7)
#plot_ROC('ZGEO-250','ZGEO-500','ZGEO-850','ZGEO','22','ACOR')
#
#plt.subplot(6,2,9)
#plot_ROC('UVEL-250','UVEL-500','UVEL-850','UVEL','22','ACOR')
#
#plt.subplot(6,2,11)
#plot_ROC('VVEL-250','VVEL-500','VVEL-850','VVEL','22','ACOR')
#
## numero 26 - > relacionado a 144h
#plt.figure(figsize=(15,15))
#
#plt.subplot(6, 2, 1)
#plot_ROC('VTMP-925','VTMP-850','VTMP-500','VTMP','26','ACOR')
#
#plt.subplot(6, 2, 3)
#plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','26','ACOR')
#
#plt.subplot(6, 2, 5)
#plot_ROC('UMES-500','UMES-850','UMES-925','UMES','26','ACOR')
#
#plt.subplot(6,2,7)
#plot_ROC('ZGEO-250','ZGEO-500','ZGEO-850','ZGEO','26','ACOR')
#
#plt.subplot(6,2,9)
#plot_ROC('UVEL-250','UVEL-500','UVEL-850','UVEL','26','ACOR')
#
#plt.subplot(6,2,11)
#plot_ROC('VVEL-250','VVEL-500','VVEL-850','VVEL','26','ACOR')
#
## <><><><><><><><<><>
#
## numero 6 - > relacionado a 24h
#plt.figure(figsize=(15,15))
#
#plt.subplot(6, 2, 1)
#plot_ROC('VTMP-925','VTMP-850','VTMP-500','VTMP','6','RMSE')
#
#plt.subplot(6, 2, 3)
#plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','6','RMSE')
#
#plt.subplot(6, 2, 5)
#plot_ROC('UMES-500','UMES-850','UMES-925','UMES','6','RMSE')
#
#plt.subplot(6,2,7)
#plot_ROC('ZGEO-250','ZGEO-500','ZGEO-850','ZGEO','6','RMSE')
#
#plt.subplot(6,2,9)
#plot_ROC('UVEL-250','UVEL-500','UVEL-850','UVEL','6','RMSE')
#
#plt.subplot(6,2,11)
#plot_ROC('VVEL-250','VVEL-500','VVEL-850','VVEL','6','RMSE')
#
## numero 10 - > relacionado a 48h
#plt.figure(figsize=(15,15))
#
#plt.subplot(6, 2, 1)
#plot_ROC('VTMP-925','VTMP-850','VTMP-500','VTMP','10','RMSE')
#
#plt.subplot(6, 2, 3)
#plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','10','RMSE')
#
#plt.subplot(6, 2, 5)
#plot_ROC('UMES-500','UMES-850','UMES-925','UMES','10','RMSE')
#
#plt.subplot(6,2,7)
#plot_ROC('ZGEO-250','ZGEO-500','ZGEO-850','ZGEO','10','RMSE')
#
#plt.subplot(6,2,9)
#plot_ROC('UVEL-250','UVEL-500','UVEL-850','UVEL','10','RMSE')
#
#plt.subplot(6,2,11)
#plot_ROC('VVEL-250','VVEL-500','VVEL-850','VVEL','10','RMSE')
