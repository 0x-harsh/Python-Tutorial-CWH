# Tuple: tuple is collection of data like lists, but unlike lists its immutable (can't be changed)

b = (1,)

a = (1, 2, 3, 6)
print(a, b)

t = (2, 45, 994, False, "Rohan", "Shivam")
# t[0] = 99 # not possible
print(t)

num = t.count(45)
print(num)

# i = t.index(99994)
# print(i) # index error

print(len(t))