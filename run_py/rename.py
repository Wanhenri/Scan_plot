#retirado trecho do site: http://ufpr3d.blogspot.com/2010/05/script-python-parta-mudar-extensao-e.html

import re
import string
import os

# Coloque os seus parametros aqui...
diretorio = "/home/wanderson/teste/data/tt/dadosscantec/"
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
