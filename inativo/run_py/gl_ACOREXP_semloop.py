import csv
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('data/dadosscantec/ACOREXP2h_20150504062015053100T.csv')
df2 = pd.read_csv('data/dadosscantec/ACOREXP6h_20150504062015053100T.csv')
df3 = pd.read_csv('data/dadosscantec/ACOREXP10h_20150504062015053100T.csv')
df4 = pd.read_csv('data/dadosscantec/ACOREXP14h_20150504062015053100T.csv')
df5 = pd.read_csv('data/dadosscantec/ACOREXP18h_20150504062015053100T.csv')
df6 = pd.read_csv('data/dadosscantec/ACOREXP22h_20150504062015053100T.csv')
df7 = pd.read_csv('data/dadosscantec/ACOREXP26h_20150504062015053100T.csv')

#list_.append(df)
ts1 = df1.loc[0:107,['VTMP-500']]
ts2 = df2.loc[0:107,['VTMP-500']]
ts3 = df3.loc[0:107,['VTMP-500']]
ts4 = df4.loc[0:107,['VTMP-500']]
ts5 = df5.loc[0:107,['VTMP-500']]
ts6 = df6.loc[0:107,['VTMP-500']]
ts7 = df7.loc[0:107,['VTMP-500']]


plt.plot(ts1,'k--', ts2,'r-',ts3,'g-',ts4,'b-',ts5,'y-',ts6,'c-',ts7,'m-')
