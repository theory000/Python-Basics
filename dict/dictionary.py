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
