import glob
import pandas as pd

#corrigir script para o modelo atual

path ='.'
allFiles = glob.glob(path + "/*.scam")

list_ = []

for file_ in allFiles:
    df = pd.read_csv(file_,delimiter='\s+')
    df.to_csv('new_file/'+file_ + '.csv', float_format='%g')
    
