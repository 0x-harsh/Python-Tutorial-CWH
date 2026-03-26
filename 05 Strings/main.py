a = "Hello"
b = 'Hello'
c = '''Hello'''

print(a, b, c)

name = "Harsh"

nameShort = name[0:3] # starts from index 0 all the way till 3 (excluding 3)
char1 = name[1]
print(nameShort)
print(char1)

print(name[:4]) # [:4] same as [0:4]
print(name[1:]) # [1:] same as [1:length]

word = "amazing"
print(word[1:6:2]) #mzn

# STRING FUNCTIONS
username = 'harshdhiman'

print(len(username)) # 11
print(username.endswith("man")) # True
print(username.startswith("har")) # True
print(username.capitalize())
print(username.find("s"))
print(username.replace("harsh", "hrsh"))

# ESCAPE SEQUENCE CHARACTERS IN PYTHON
a = "Harry is a good boy \nbut not a bad boy"
print(a)

# \n : for new line
# \t : for tab like space
# \' : for single quote
# \\ : for backslash