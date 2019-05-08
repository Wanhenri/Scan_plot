import json
from pprint import pprint
import itertools

with open('json/teste.json', encoding='utf-8') as f:
    data = json.load(f)




def select(teste1,teste3,teste4,teste5):
  result1 = []
  result2 = []
  result3 = []
  result4 = []
  result5 = []
 
  for a in range(0,teste1): 
    var1 = data['var_scantec'][0]['position'][a]
    result1.append(var1)

    var2 = data['var_scantec'][1]['previsao'][a]
    result2.append(var2)

  for c in range(0,teste3):    
    var3 = data['var_scantec'][2]['estatistica'][c]
    result3.append(var3)
  
  for c in range(0,teste4):    
    var4 = data['var_scantec'][3]['title'][c]
    result4.append(var4)
  
  for e in range(0,teste5):    
    var5 = data['var_scantec'][4]['level'][e]
    result5.append(var5)

  return (result1,result2,result3,result4,result5)   

