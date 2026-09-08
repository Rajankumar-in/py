# sets: there is no way to change the items in sets
#       sets are unordered
#       sets are unindexed
#       sets cannot contain the duplicate value
#       s = {1,3,2,4} <--- examoples


s = {1,32,483,"rajan",37, 74,}
print(s)

print(type(s))
s.add(566)
print("after using the add method", s)
s.remove(32)
print("after using the remove method", s)

# clear methos will slear the sets
s.clear()
print("after using the clear method in sets" ,s)

#to check that sets cannot contail the duplicate value , we will use "union method"
#we can also chek without the union method only filling the repeted value in set then run the program. you will see the magic
s1 = {1,3,4,5,2,4,1,4,2}
s2 = {10,11,21,5,1,3,4,50}
print("the type of s1 sets:", s1,type(s1))
print("the type of s2 sets:", s2, type(s2))

print("after using the union method ", s1.union(s2))
# intersection method ( this will find the common value in both sets s1 and s2)
print("after applying the intersection method", s1.intersection(s2))
