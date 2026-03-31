censor_words = [
    "idiot", "stupid", "dumb", "jerk", "moron", 
    "shut up", "hell", "damn", "crap", "bastard", 
    "loser", "suck", "garbage", "trash", "hate"
]

with open("five.txt") as f:
    content = f.read()

for word in censor_words:
    content = content.replace(word, "#" * len(word))

with open("five.txt", "w") as f:
    f.write(content)