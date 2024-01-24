x = input("First Number: ")
y = input("Second Number: ")

print(int((float(x) + float(y))))

'''
Here we give our first input and second input if our input contain a floating point '.' then the int() will convert it into a integer.
'''

# same code with more simplified, look kinda complicated.
print(int(float(input("First Number: ")) + float(input("Second Number: "))))