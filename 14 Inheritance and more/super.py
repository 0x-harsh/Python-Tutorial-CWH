class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__() # used to run parent class methods
        print("Constructor of Manager")
    c = 3

# p = Programmer()
m = Manager()