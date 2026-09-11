# write a program to generate the multiplication table from 2 t0 20 and write it to the different
# file. place this file in a folder for 13 years old...

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2, 21):
    generateTable(i)
