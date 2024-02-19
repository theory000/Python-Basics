names = ["Carter", "David", "John"]
# We'll give a input i.e. "david" and the capatilize() function will make the first word capital and iterate over the dir to find that name and in second method use simple if statement.
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