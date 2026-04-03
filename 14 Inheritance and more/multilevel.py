class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

p = Programmer()
m = Manager()

print(p.a)
print(p.b)

print(m.a)
print(m.b)
print(m.c)