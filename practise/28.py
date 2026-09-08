# write a program to find the factprial of a given no. using for loop
# 5! = 1 x 2 x 3 x 4 x 5

n = int(input("enter a no.: "))
product = 1
for i in range(1, n+1):
    product = product * i
print(f"the factorial of {n} is {product}")
