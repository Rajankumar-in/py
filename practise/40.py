# write a python program to print the multiplication table of the given no.

def multiply(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")


n = int(input("enter a no.:"))
print(multiply(n))
