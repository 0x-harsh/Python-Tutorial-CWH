a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if(b == 0):
    raise ZeroDivisionError("Can't divide by zero")
print(f"The division {a}/{b} is {a/b}")