# Dictionary: set of properties, property: key value pair

marks = {
    "Harsh": 99,
    "Amit": 98,
    "Kashish": 100,
    "Neha": 99
}

print(marks, type(marks))

print(marks["Harsh"])

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({
    "Harsh": 93,
    "Renuka": 100
})

print(marks)

# print(marks.get("Harsh1")) # returns None
# print(marks["Harsh1"]) # returns an error