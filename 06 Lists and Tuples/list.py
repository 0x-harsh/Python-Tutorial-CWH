friends = ["apple", "orange", 5, 34.5, False]
# Lists are mutable

print(friends[0])

friends[0] = "Grappes"

print(friends[0])

print(friends[1:4])

friends.append("Harry")

print(friends)

list1 = [1, 23, 45, 1, 3, 5]
# list1.sort()
# list1.reverse()
# list1.insert(3, 3333) # insets 3333 at index 3 in the list1
value = list1.pop(3) # removes value at index 3
print("value:", value)

print(list1.remove(5)) # remves 5 from the list if it exists in the list, and returns None

print(list1)