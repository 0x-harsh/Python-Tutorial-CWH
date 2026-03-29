name = input("Enter your name: ")

def greet(name = "Harsh Dhiman"): # default value
    print(f"Good Day, {name}")
    return "Ok"

b = greet()
a = greet(name)
print(a)