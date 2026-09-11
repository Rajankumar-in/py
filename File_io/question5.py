# to check the given file that "python" word is available or not


with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("yes, python is present")

else:
    print("no, python is not present")
