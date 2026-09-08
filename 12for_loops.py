for i in range(4):
    print(i)
print("counting ends here")


# for loops with list

l = [ 1,4,34,55,"rajan"]
for i in l:
    print(i)
print("for loops with list end here")

## for loops with strings
s = "harry"
for i in s :
    print(i)



### for loops with else statement, this will run when the loops exhaust

l =[1,5,8]
for item in l:
    print(item)
else:
    print("done")  #this will run when the loops exhaust


### break statement in for loops

for i in range(100):
    if(i ==34):
        break  #exit the loop right now
    print(i)

### continue statement in for loop

for i in range(100):
    if(i ==34):
        continue  # here this will skip iteration 34
    print(i) 


## pass statement in for loop
# pass is a null statement , it instructs to "do nothing", without pass the program

for i in range(750):
    pass # there is not complete code but it has skip this and run it



i = 0
while(i<45):
    print(i)
    i+=1


