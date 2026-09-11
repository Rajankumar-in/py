#write a python program to copy the file "this.txt"


# this command will open the created file "this.txt" and read the content in it
with open("this.txt") as f:
    content = f.read()

# this command will create a new file "this_copy.txt" and write the contend of this.txt in new file , means copy that...
with open("this_copy.txt", "w") as f:
    f.write(content)
