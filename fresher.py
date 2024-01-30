# Calculator

# add
def add(x, y):
    return x + y
# subtract
def sub(x, y):
    return x - y
# multiply
def multi(x, y):
    return x * y
# divide
def div(x, y):
    if (x == y):
        return "Cannot divide by zero"
    else:
        return x / y
    
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3' , '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result", add(num1, num2))
        elif choice == '2':
            print("Result", sub(num1, num2))
        elif choice == '3':
            print("Result", multi(num1, num2))
        elif choice == '4':
            print("Result", div(num1, num2))
    else:
        print("Invalid input")