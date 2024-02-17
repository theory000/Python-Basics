# HARVARD CS50 COURSE

s = input("Do you agree? ")

if s == 'Y' or s == 'y':
    print('Agreed.')
elif s == 'N' or s == 'n':
    print('not agreed.')

# OR
    
x = input('Do you agree? ').lower()

if x in ['y', 'yes']:
    print("Agree.")
elif x in ['N', 'no']:
    print("Not agree.")
# ---------------------------------

for i in range(3):
    print('meow')
# ---------------------------------

def dog():
    print('bark')

for i in range(3):
    dog()
#----------------------------------
    
def main():
    theory(3)

def theory(n):
    for i in range(n):
        print('theory')

main()
#---------------------------------

before = input("Before: ")
print("After: ", end="")
for c in before:
    print(c.upper(), end="")
print()
#OR
before = input("Before: ")
print(f"After: {before.upper()}")
#---------------------------------

def main():
    meow(3)

def meow(n):
    for i in range(n):
        print("meow")
main()
#--------------------------------

x = 2
y = 13
z = x / y

print(f"{z:.50f}")
#--------------------------------

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Not an integer")


def main():
    x = get_int("x: ")
    y = get_int("y: ")

    print(x + y)

main()
#-------------------------------

scores = [72,45,34]

average = sum(scores) / len(scores)
print(f"Average: {average}")