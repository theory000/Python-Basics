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

scores = []
for i in range(3):
    score = int(input("Score: "))
    scores.append(score)

print(scores)

average = sum(scores) / len(scores)
print(f"Average: {average}")
#---------------------------------

names = ["Carter", "David", "John"]
# We'll give a input i.e. "david" and the capatilize() function will make the first word capital and iterate over the array to find that name and in second method use simple if statement.
name = input("Name: ").capitalize()

# This is First method
# for n in names:
#     if name == n:
#         print("Found")
#         break
# else:
#     print("Not Found")

# This is second method
if name in names:
    print("Found")
else:
    print("Not Found")
#---------------------------------
    
people = [
    {"name": "Carter", "number": "03044950486"},
    {"name": "David", "number": "0354234086"},
    {"name": "John", "number": "0304234486"},
]

name = input("Name: ").capitalize()

for person in people:
    if person["name"] == name:
        number = person["number"]
        print(f"Found {number}") # OR print(f"Found {person['number']})
        break
else:
    print("Not found")

# Simplified Method

peoples = {
    "Rehan": "030345446577",
    "Fizze": "030345475448",
    "Salman": "030348787877",
}

names = input("Name: ").capitalize()

if names in peoples:
    numbers = peoples[names]
    print(f"Found {numbers}")
else:
    print("Not found")
