l = [3, 343, 45, 214]

# index = 0
# for item in l:
#     index = index + 1
#     print(f"The item number {index} is {item}")

# THIS CAN BE SIMPLIFY USING ENUMERATE FUNCTION

for index, item in enumerate(l):
    print(f"The item number {index} is {item}")