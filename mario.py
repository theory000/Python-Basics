def main():
    height = get_height()
    for i in range(height):
        print("#")

def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                return n
        except ValueError:
            print("Value is not integr")

main()
# -------------------------------------

for i in range(2):
    print("?", end="f")

# OR
print("?" * 4)
# -------------------------------------

# row and column
for k in range(3):
    for j in range(3):
        print("#", end="")
    print("")

# OR
for l in range(3):
    print("|" * 4)