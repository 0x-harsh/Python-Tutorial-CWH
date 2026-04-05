from functools import reduce

# MAP => map applies a function to all the items in an input-list

l = [12, 23, 34, 45, 56, 67, 78, 89, 90]
square = lambda n: n * n
sqList = map(square, l)
print(list(sqList))

# FILTER => filter returns the items that return true for a condition

def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

# REDUCE => reduce function performs an operation on all the elements and returns a single number (eg. adding all the items in a list)

def sum(a, b):
    return a + b

print(reduce(sum, l))