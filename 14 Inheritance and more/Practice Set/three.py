class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + (self.salary * (self.increment/100)))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = (((salary/self.salary) - 1) * 100)

e = Employee()
print(e.salaryAfterIncrement)

e.salaryAfterIncrement = 280
print(e.increment)

# new = old + old * (increment/100)
# new = old * (1 + (increment/100))
# (((new/old) - 1) * 100) = increment