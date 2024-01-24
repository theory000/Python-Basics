def sum_all(*numbers):
  total = 0
  for number in numbers:
    total += number
  return total

# Call the function with a variable number of arguments
result = sum_all(1, 2, 3, 4, 5)

print(result)


# A variable-length argument is a function argument that can accept any number of values.