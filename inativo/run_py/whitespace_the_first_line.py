import re

with open('ACOREXP10h_20150504062015053100T.csv', "r") as in_file:
    with open('teste_2.txt', "w") as out_file:
        for word in in_file:
          char = re.sub(r"^\s+", "", word, flags=re.I) #REGEX
          char1 = char.replace("    ",", ")
          print(char1)
          out_file.write(char1)
         
