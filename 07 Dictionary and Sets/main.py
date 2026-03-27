# sets: set is a collection well-defined objects, unique values only (no repitition of same values)

s = {} # Empty dictionary

set1 = {12, 34, 45}
print(set1, type(set1))

e = set()
print(e, type(e))

set2 = {5, 5, 5, 5, 1, 2, 4, 6, 3, 2, 2, 3, 2, 4, 'Harsh'}
print(set2) # {1, 2, 3, 4, 5, 6}

set2.add(556)
print(set2)

s1 = {23, 45, 67, 78}
s2 = {12, 34, 67, 78}
print(s1.union(s2))
print(s1.intersection(s2))