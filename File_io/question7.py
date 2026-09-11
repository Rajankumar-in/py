#write  a profram to find out whether a file is identical & matches the content of another file

#file1.txt
#file2.txt

with open("file1.txt") as f:
    content1 = f.read()

with open("file2.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("yes, the given files are identical")

else:
    print("no, the given files are not identical")

