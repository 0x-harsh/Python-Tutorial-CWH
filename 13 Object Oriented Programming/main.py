# OOPs in python

class Employee:
    language = "Python"
    salary = 120000

    # dunder method or constructor
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


harry = Employee("Harry", 120000, "Python") 
harry.getInfo()
Employee.greet()

rohan = Employee("Rohan", 130000, "Java")   
print(rohan.salary)

harsh = Employee("Harsh", 150000, "JavaScript") 
print(harsh.salary)