# generate a random number
# get input from user
# compare input number with generated number
#     if equal user win
#     if input number is less than generated number throw LESS
#     if input number is greater than generated number throw HIGH
# count number of gueses util user guess the right
# less count means great

import random

randomNum = random.randint(1, 100)
count = 0
while(True):
    inputNum = int(input("Guess the number: "))
    count = count + 1

    if(inputNum < randomNum):
        print("Your guess is low")
    elif(inputNum > randomNum):
        print("Your guess is high")
    elif(inputNum == randomNum):
        print("Your guess is correct, you win!")
        break
    else:
        print("Invalid input")

print(f"You guess the number {randomNum} in {count} attempt(s)")