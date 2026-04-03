class Employee:
    company = "ITC"
    name = "Harsh"
    salary = 1200000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

class Coder:
    language = "python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")

# INHERITANCE
class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language}")


a = Employee()
b = Programmer()

print(a.company, b.company)
b.show()
b.showLanguage()
b.printLanguages()