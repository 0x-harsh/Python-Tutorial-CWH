f = open("file.txt")
print(f.read())
f.close()

# The same thing can be written using with statement like this:
with open("file.txt") as f:
    print(f.read())

# we don't have to explicitly close the file