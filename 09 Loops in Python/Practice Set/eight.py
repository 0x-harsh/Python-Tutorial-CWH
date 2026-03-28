# ***
# * *
# ***

num = int(input("Enter number: "))

for i in range(1, num+1):
    if(i!=1 and i!=num):
        print("*", end="")
        print(" "* (num-2), end="")
        print("*", end="")
    else:
        print("*"* num, end="")
    print("")