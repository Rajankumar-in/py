# write a programm to rename the file to "renamed_by_python.txt"

# now "test.txt" file is creating to rename it


with open("test.txt") as f:
    content = f.read()



with open("renamed_by_python.txt", "w") as f:
    f.write(content)


