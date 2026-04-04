# WALRUS OPERATOR [:=] - Introduced in Python 3.8

if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"list is too long ({n} elements, expected <= 3)")

# TYPES DEFINITION IN PYTHON

n : int = 5 # type of n is int

name : str = "Harry" # type of name is str

def sum(a: int, b: int) -> int:
    return a + b