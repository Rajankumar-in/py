#write a program to fill in a letter template 
#letter = '''Dear <|Name|>,
#You are selected!
#Date: <|Date|>
#'''

#----------->---------------->-------------------------

letter = '''Dear <|Name|>,
You are selected!
Date: <|Date|>
''' 
print(letter.replace("<|Name|>", "Rajan") .replace("<|Date|>", "20 october 2026"))
