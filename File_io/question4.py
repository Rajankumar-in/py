# a file content a new word "Donkey" multiple times. you need to write a program which replace
# "#####" by updating the same file

word = "Donkey"
with open("filedonkey.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "#####")

with open("filedonkey.txt", "w") as f:
    f.write(contentNew)


