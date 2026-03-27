p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comment: ")
messageLower = message.lower()

if((p1 in messageLower) or (p2 in messageLower) or (p3 in messageLower) or (p4 in messageLower)):
    print("spam!")

else:
    print("not a spam!")