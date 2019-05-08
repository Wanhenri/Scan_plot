with open('ACOREXP10h_20150504062015053100T.csv', "r") as in_file:
    with open('teste.txt', "w") as out_file:
        for word in in_file:
          char = word.replace("    ",", ")
          print(char)
          out_file.write(word.replace("    ",", "))
                                                      
