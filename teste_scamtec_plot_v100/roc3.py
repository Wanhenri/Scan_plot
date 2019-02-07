import re
import string
import os

# Coloque os seus parametros aqui...
diretorio = "."
extensao = ".*scam"
novaExtensao = ".csv"  # nesse caso eh vazia

# Muda extensao
reg = re.compile(extensao)
if os.path.isdir(diretorio) and not os.path.islink(diretorio):
    arquivos = os.listdir(diretorio)
    for arquivo in arquivos:
        newExt = re.compile(extensao).match
        if newExt(arquivo):
            c = os.path.splitext(arquivo)
            b = c[0] + novaExtensao
            a = os.path.join(diretorio,arquivo)
            b = os.path.join(diretorio,b)
            os.rename(a,b)

#
#ainda melhorando essa segunda parte
#

with open('RMSEEXP01_20150501122015050112T.csv', "r") as in_file:
    with open('RMSEEXP01_20150501122015050112T_1.csv', "w") as out_file:
        for word in in_file:
          
          char = re.sub(r"^\s+", "", word, flags=re.I)
         #retira os 4 espacos em brancos existentes
          char1 = char.replace("   "," ")
         #retira 2 espacos em brancos que restaram
          char2 = char1.replace("  "," ")
         # susbtitui os NaN por 0
          char3 = char2.replace("NaN","0")
         # acrescenta virgula + espaco nos espacos em branco
          char4 = char3.replace(" ",", ")

          #print(char4)
          out_file.write(char4)
