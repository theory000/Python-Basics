num = int(input("Number is between: "))
if num < 0:
    print("number is negative")
elif num > 0:
    if num <= 10:
        print("Number is between 1-10")
    elif num > 10 and num <= 20:
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Zero")