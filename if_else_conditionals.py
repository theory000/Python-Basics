a = int(input("Enter your age: "))
print("your age is:", a)

if a==18:
    print("You can drive")
else:
    print("You cannot drive")


marks = 249
pass_marks = 250

if (marks<pass_marks):
    print("you are fail")
else:
    print("you passed")


applePrice = 10
budget = 200
if budget - applePrice > 50:
    print('Alexa add 1 kg to the cart')
elif budget - applePrice > 70:
    print("its ok you can buy")
else:
    print('Alexa do not add apples to the cart.')

num = int(input("Enter the value of num: "))
if num < 0:
    print("Number is negative.")
elif num == 0:
    print("Number is Zero.")
elif num == 999:
    print("Number is Special <3")
else:
    print("Number is positve.")


myMarks = int(input("My marks are: "))
passMarks = 40
totMarks = 50

if (myMarks < passMarks):
    print("You fail")
elif (myMarks > passMarks) and (myMarks < totMarks): #we will get pass even if we write 50 so to bypass that we'll use and and less then totMarks hehe OR we can just put "very good" elif before "pass" elif then we dont need and.
    print("you pass")
elif (myMarks == totMarks):
    print("very good")
else:
    print("error")