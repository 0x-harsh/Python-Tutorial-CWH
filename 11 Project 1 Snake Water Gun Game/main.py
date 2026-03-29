import random

print("SNAKE WATER GUN Game")
print("'s' for Snake")
print("'w' for Water")
print("'g' for Gun")
youStr = input("Enter your choice: ")

gameDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

youDict = {
    "s": 1,
    "w": -1,
    "g": 0
}
computer = random.choice([-1, 0, 1])
you = None

if(youStr == "s" or youStr == "w" or youStr == "g"):
    you = youDict[youStr]
    print(f"You chose: {gameDict[you]}\nComputer chose: {gameDict[computer]}")
else:
    print("Enter correct choice!")

if(computer == you):
    print("Game Draw!!")

else:
    if(computer == -1 and you == 1):
        print("You Won!")

    elif(computer == -1 and you == 0):
        print("Computer Won!")

    elif(computer == 1 and you == -1):
        print("Computer Won!")

    elif(computer == 1 and you == 0):
        print("You Won!")

    elif(computer == 0 and you == 1):
        print("Computer Won!")

    elif(computer == 0 and you == -1):
        print("You Won!")

    else:
        print("Something went wrong!")