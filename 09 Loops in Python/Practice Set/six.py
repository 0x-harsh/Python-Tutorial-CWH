# *
# ***
# *****

num = int(input("Enter number: "))

# for i in range(1, num+1):
#     for j in range(1, (2*i)):
#         print("*", end="")
    
#     print("")

for i in range(1, num+1):
    print(" "* (num-i), end="")
    print("*"* (2*i-1), end="")
    print("")