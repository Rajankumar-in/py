# write a python program to find the greatest of the four no. entered by the users

a = int(input("enter the first no."))
b = int(input("enter the second no."))
c = int(input("enter the third no."))
d = int(input("enter the fourth no."))

if(a>b and a>c and a>d):
    print("the first no. is greatest: ", a)
elif(b>c and b >d and b>a):
    print("the second no. is greatest: ", b)
elif(c>d and c>a and c>b):
    print("the third no. is greatest: ", c)
else:
    print("the fourth no. is greatest: ", d)

