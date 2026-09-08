# function is a group of statement performing a specific task when a program gets bigger in size 
# and its complexity grows, its get difficult to track that which code is doing what...

'''
# if i have to run it for the multiple person and multiple times

a = int(input("enter your no."))
b = int(input("enter your no."))
c = int(input("enter your no."))
average = (a+b+c)/3
print("average")

a = int(input("enter your no."))
b = int(input("enter your no."))
c = int(input("enter your no."))
average = (a+b+c)/3
print("average")

.......
.......

'''
#if we dont want to do the same repeated code the u should use function like this
#-----> function defenation --------->
def avg():
    a = int(input("enter your no."))
    b = int(input("enter your no."))
    c = int(input("enter your no."))
    avgerage = (a+b+c)/3
    print(avgerage)


# ------> avg() ----> function call hai
avg()
# if u want to run this 5 times the replicate  avg() 5 times , now see the magic
avg()
print("thank u")
avg()
print("thank u")
avg()
print("thank u")
avg()
avg()




# note : there are two types of function
#       1. build in function    : already available in python
#           examples:   print , range ,  
#       2. user define function : function create by the user
#           examples: avg() ...
