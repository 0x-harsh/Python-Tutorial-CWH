f = open("poem.txt")
poem = f.read()
if("twinkle" in poem):
    print("The word twinkle is present in the content")
else:
    print("The word twinkle is not present in the content")
f.close()