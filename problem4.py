"""write a program to print a connectors of a directory usine os module. 
search online for the function which does that"""
import os

# Specify the directory path
path = "/"

# Get contents of the directory
contents = os.listdir(path)

# Print each item
for item in contents:
    print(item)
