# write a program to input eight no of forms the user and display all the unique numbers (once)

s = set() #empty set

n = input("enter number: ")
s.add(int(n))
n = input("enter number: ")
s.add(int(n))
n = input("enter number: ")
s.add(int(n))
n = input("enter number: ")
s.add(int(n))
n = input("enter number: ")
s.add(int(n))
n = input("enter number: ")
s.add(int(n))
n = input("enter number: ")
s.add(int(n))
n = int(input("enter number: "))
s.add(n)

print(s)
