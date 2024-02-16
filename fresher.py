# x = input("Do you agree> ").lower() # First way

# x = x.lower() # Second way

# if x in ["y", "yes"]:
#     print("Agreed")
# elif x in ["n", "no"]:
#     print( "Not agreed")

# 1:01:32
    
# for i in range(3):
#     print("Hello World")

before = input("Before: ")
print("After: ", end="")
for c in before:
    print(c.upper(), end="")