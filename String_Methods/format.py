age = 36
txt = "The number represents: " , age
print(type(txt)) # tuple

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
txt = "the num {}"
print(type(txt.format(age))) # str

#Working with multiple formats

name = "theory"
age = 18
place = "karachi"
thing = "coding"

combine = "{} is {} years old and he live in {} and loves {}"
print(combine.format(name, age, place, thing))