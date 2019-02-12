import glob
import pandas as pd
import os

#corrigir script para o modelo atual - Nok
#corrigir diretorio                  - Nok
#corrigir nome do file de saida      - ok

path ='.'
allFiles = glob.glob(path + "/*.scam")

list_ = []

for file_ in allFiles:
    name_file=os.path.splitext(file_)[0]
    df = pd.read_csv(file_,delimiter='\s+')
    df.to_csv('new_file/'+name_file + '.csv', float_format='%g')
    
