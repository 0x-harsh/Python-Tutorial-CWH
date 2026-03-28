# FOR LOOP
for i in range(1, 6):
    print(i) # from 1 to 5

print("----------")

# WHILE LOOP
i = 1
while(i<6):
    print(i)
    i = i + 1

print("-----------")

for i in range(0, 20, 4):
    print(i)

print("-----------")

l = [2, 4, 6, 9, 2, 4]
for i in l:
    print(i)

print("-----------")

t = (23, 43, 45, 65, 87)
for i in t:
    print(i)

print("-----------")

s = "harshdhiman"
for i in s:
    print(i)

li = [1, 7, 8]
for i in li:
    print(i)
else:
    print("DONE") # this is printed when the loop exhausts!

# break => abruptly exits the loop
# continue => skips an iteration
# pass => pass is null statement in python it instructs to do nothing

print("----------")

for i in range(10):
    if(i == 3):
        break
    print(i)

print("----------")

for i in range(10):
    if(i == 3):
        continue
    print(i)

print("----------")

for i in range(1, 5):
    pass

print("----------")

iter=0
while (iter<6):
    print(iter)
    iter = iter + 1