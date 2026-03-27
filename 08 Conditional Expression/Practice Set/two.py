marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

totalPercentage = (100*(marks1 + marks2 + marks3))/300

if(totalPercentage>=40 and (marks1>=33 and marks2>=33 and marks3>=33)):
    print(f"You are pass, percentage: {totalPercentage}")
else:
    print(f"You failed, try again next year, percentage: {totalPercentage}")