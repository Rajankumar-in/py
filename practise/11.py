#write a program to accept marks of 6 students and display them in sorted manner
from turtle import st


students = []
s1 =int((input("the marks of 1st student: ")))
students.append(s1)
s2 =int((input("the marks of 2nd student: ")))
students.append(s2)
s3 =int((input("the marks of 3rd student: ")))  
students.append(s3)
s4 =int((input("the marks of 4th student: ")))
students.append(s4)
s5 =int((input("the marks of 5th student: ")))
students.append(s5)
s6 =int((input("the marks of 6th student: ")))
students.append(s6)

print("the marks of all 6 students are --->", students)
students.sort()
print("the marks of all 6 students in a sorted manners are --->",students)

