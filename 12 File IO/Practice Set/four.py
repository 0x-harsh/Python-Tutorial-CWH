word = "Donkey"
newWord = "######"

with open("donkey.txt") as f:
    content = f.read()

contentNew = content.replace(word, newWord)

with open("donkey.txt", "w") as f:
    f.write(contentNew)