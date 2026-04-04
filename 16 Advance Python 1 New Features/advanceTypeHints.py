from typing import List, Union, Tuple, Dict

# list of integers
numbers: List[int] = [1, 2, 3, 4, 5, 6]

# tuple of  a string and an integer
person: Tuple["str", int] = ("Alice", 34)

# dictionary with string key and int value
scores: Dict[str, int] = {"Alice": 90, "Bob": 87}

# Union type for variables that can hold multiple types
identifier: Union[int, str] = 'ID123'
identifier = 12345 #Also valid