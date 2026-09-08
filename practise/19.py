#write a python program wheather a student is pass or fail  (3 subject , 33% each sub = pass means 40% total)

marks1 = int(input("enter marks 1: "))
marks2 = int(input("enter marks 2: "))
marks3 = int(input("enter marks 3: "))

# check for the total %
total_percentage = (marks1 + marks2 + marks3)/3

if(total_percentage >= 40 and marks1 > 33 and marks2 > 33 and marks3 > 33 ):
    print("ypu are pass with", total_percentage )
else:
    print("you failed and have only", total_percentage)
