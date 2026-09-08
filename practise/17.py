# create an empty dictonary allow 4 friends to enter htir favourite language as value and use keys as their names , assume that the names are unique
d = {}

name = input("enter your name :")
language = input("enter the favourite language :")
d.update({name: language})

name = input("enter your name :")
language = input("enter the favourite language :")
d.update({name: language})

name = input("enter your name :")
language = input("enter the favourite language :")
d.update({name: language})

name = input("enter your name :")
language = input("enter the favourite language :")
d.update({name: language})

print(d)


# if the name is repeted then the last value will be applicable , 
# because of the update method are being used. 
