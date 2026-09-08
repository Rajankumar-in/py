#write a py program that the given no. is prime or not
#prime no. = dividen by 1 ya fir wo khud divide kr raha ho

n = int(input("enter a no.:"))

for i in range (2, n):
    if(n%i) == 0:
        print("number is not a prime no.")
        break
else:
    print("given no. is prime")

