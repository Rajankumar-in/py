# there are three types of string in python
a = 'rajan'
b = "rajan"
c = """Rajan"""
print (a)
print(len(a)) #length function
print(type(a))

nameshort = a[0:3] #3th index tk ka character print karega
print(nameshort)
charactor1 = nameshort[1] #counting will always start from zero
print(charactor1)


# negative slicing in string

name ="rajan"
nameshort1 = name[-5:-1] #ye 1st index se 5th index tk print karega aur ye reverse me hai isliye kuch bhi print nahi karega.
print(nameshort1) #ye kuch bhi print nahi karega kyuki ye 1st index se 5th index tk print karega aur ye reverse me hai isliye kuch bhi print nahi karega.

print(b.replace("rajan", "Rajan")) # replace function 
print(a.upper()) #upper function
print(c.lower()) #lower function
print(a.capitalize()) #capitalize function
print(a.count("a")) #count function
print(a.endswith("n")) #endswith function
print(a.endswith("j"))
print(a.startswith("r")) #startswith function
print(a.startswith("R")) #startswith function
