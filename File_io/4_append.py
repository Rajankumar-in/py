# this will add string to my old file "myfile.txt"
# to add new string to the file


st = "hey Anand you are amazing"
f = open("myfile.txt", "a")

f.write(st)

f.close()

# more modes of opening files
# r - open for reading
# w - open for writinng
# a - open for appending
# + - open for updating
# rb - will open for read for binary mode
# rt - will open for read in text mode
