def generateTable(num):
    table = ""
    for i in range(1, 11):
        table = table + f"{num} x {i} = {num*i}\n"

    # tables folder should exists first before running the program
    with open(f"tables/table_{num}.txt", "w") as f:
        f.write(table)

for num in range(2, 21):
    generateTable(num)