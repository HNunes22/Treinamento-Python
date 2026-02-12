# Lambda
#                       parame: expressao
multiply_numbers = lambda x, y: x * y

print(multiply_numbers(3, 3))

# Map()

listNumbers = [1, 2, 3, 4, 5, 6,  7, 8, 9,  10]
newListNumbers = list(map(lambda x:  x * 2, listNumbers))
print(newListNumbers)

# Filter

filterListNumbers = list(filter(lambda x: x < 5, listNumbers))
print(filterListNumbers)

