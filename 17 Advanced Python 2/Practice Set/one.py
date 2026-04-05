try:
    name = str(input("Enter your name: "))
    marks = int(input("Enter marks: "))
    phone = int(input("Enter phone number: "))
except Exception as e:
    print(e)

output = "The name of the student is {0}, his marks are {1}, and phone number is {2}".format(name, marks, phone)
print(output)