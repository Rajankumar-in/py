#write a python program to create a dictionary of student names and their marks
marks ={ 
    "rajan": 100,
    "rohit": 90,        
    "sachin": 80,
    "virat": 70
}

print("the marks of the students are: ", marks)
print(type(marks))

# properties of the python dictionary
# 1. dictionary is a collection of key value pairs
# 2. dictionary is unordered
# 3. dictionary is mutable
# 4. dictionary is indexed
# 5. can not store duplicate keys in dictionary

#methods

print(marks.items()) # it will return the list of tuples of key value pairs
print(marks.keys()) # it will return the keys or container in which the value is stored
print(marks.values()) # it will shows the values in a array
print(marks.update({"rajan": 101}))
print(marks)
print(len(marks))

