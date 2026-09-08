# what will be the length of the following set as 
# s = { 20, 20.0, '20'}

s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(s)
print("the length of s = ", (s))
print(len(s))

# in python 1 = 1.0 , because the comparison operator only check the value , they not need to datatype
s1 = {}
print(type(s1))
