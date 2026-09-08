#write a program to assign the grade to the student according to the marks they got
marks = int(input("enter the total marks you got:"))

if(marks >= 80 and marks <= 100):
    print("your grade is E")
elif(marks >= 70 and marks < 80):
    print("your grade is O")
elif(marks >= 60 and marks < 70):
    print("your grade is A")
elif(marks >= 50 and marks < 60):
     print("your grade is B")
elif(marks >= 33 and marks < 50):
    print("your grade is C")
else:
    print("you are fail")
