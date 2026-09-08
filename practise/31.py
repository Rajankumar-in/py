#write a program of a multiplication of a table using for loops in reverse order

n = int(input("enter a no.:"))

for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")

