class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

harsh = Programmer("Harsh", 150000, 110094)
print(harsh.name, harsh.salary, harsh.pincode, harsh.company)

amit = Programmer("Amit", 160000, 110095)
print(amit.name, amit.salary, amit.pincode, amit.company)

kashish = Programmer("Kashish", 170000, 110096)
print(kashish.name, kashish.salary, kashish.pincode, kashish.company)

neha = Programmer("Neha", 180000, 110097)
print(neha.name, neha.salary, neha.pincode, neha.company)