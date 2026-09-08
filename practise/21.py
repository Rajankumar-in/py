# write a program where check the username is less than 10 or not
username = input("Enter your username: ")

length=len(username)

if(length<= 10):
    print("this username is valid!")
else:
    print("this username is not valid , bcz it contains more than 10 letters")
