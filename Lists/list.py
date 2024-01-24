marks = [3,5,6,"theory",True]
print(marks[-3]) # Negative Index
print(marks[len(marks)-3]) # Positive Index
print(marks[5-5]) # Positive Index
print(marks[2]) # Positive Index
# if True in marks:
#     print("yes")
# else:
#     print("no")

if "eo" in "theory":
    print("yes")
elif "Th" in "theory":
    print("ahhh")
else:
    print("theres an error in the code")

print(marks[2:3])