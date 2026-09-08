# write a program to print a multiplication of a given no. using for loop
n = int (input("Enter a no. :"))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")
    
## write a program to read all the persos name stored in a list l which starts with "r" 
l = ["Rajan","Rajesh","david","Dhavan","Ritu","ankit","raju"]

for name in l:
    if(name.startswith("R")):
        print(f"Hello {name}")


## print a table using while loop

n = int(input("Enter a no for table using while loop: "))

i =1
while(i<11):
    print(f" {n} x {i} = {n*i}")
    i +=1
