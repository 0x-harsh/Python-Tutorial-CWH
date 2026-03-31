class Demo:
    a = 45

o = Demo()
print(o.a) # prints the class attribute a
o.a = 89 # instance attribute a is created for object o and assigned the value 89
print(o.a) # prints the instance attribute a, which is different from the class attribute a
print(Demo.a)