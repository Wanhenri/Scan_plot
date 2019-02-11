# Inicio das atividades

+ 29/01/19
+ 30/01/19
  - Ausente; Fui para são josé dos campos
+ 31/01/19
+ 01/02/19
  - Sem internet
+ 04/02/19
+ 05/02/19
+ 06/02/19
+ 07/02/19
+ 08/02/19
+ 11/09/19

---

+ position = 6, 10, 14, 18, 22, 26
+ previsao = 24, 48, 72, 96, 120, 144
+ estatistica = 'ACOR', 'RMS', 'VIEW'
+ title= "VTMP","TEMP","UMES","ZGEO","UVEL","VVEL","AGPL","PSNM-000","PSNM","PREC-000","PREC","PREV-000","PREV"
+ level =250, 500, 850, 925

## links sobre como usar json em python

---
[sobre json em python](https://developer.rhino3d.com/guides/rhinopython/python-xml-json/)

[sobre json em python](https://codingnetworker.com/2015/10/python-dictionaries-json-crash-course/)

---

+ plot_ROC_1_var('PSNM-000','PSNM','6','ACOR')
+ plot_ROC_1_var(str(a[3][7]),str(a[3][8]), a[0][0],a[2][0])
+ nao tem dados nas variaveis PREC PREV, por isso os valores 7 e 8 fixos

+ plot_ROC('TEMP-250','TEMP-500','TEMP-850','TEMP','6','ACOR')
+ title+level | title+level | title+level | title | position | estatistica
