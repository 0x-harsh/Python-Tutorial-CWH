try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)

# IF TRY SUCCESSFUL THEN OUR PRORAMS ENTER IN ELSE BLOCK
else:
    print("Iam inside else")