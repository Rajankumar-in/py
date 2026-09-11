# in read mode there is no need to write the "r" , but in the write mode there is a requirement to write "w"

f = open("file.txt")
lines = f.readlines()
# print(lines, type(lines))
 
# f.close()
#or
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()
