people = [
    {"name": "Carter", "number": "03044950486"},
    {"name": "David", "number": "0354234086"},
    {"name": "John", "number": "0304234486"},
]

name = input("Name")

for person in people:
    if person["name"] == name:
        number = person["number"]
        print(f"Found {number}")
        break
else:
    print("Not found")