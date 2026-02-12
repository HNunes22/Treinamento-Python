# Concat

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

numbers1.extend(numbers2)

print(numbers1)

print()

# Unpacking

fruits = ["Apple", "Banana", "Avocado", "Strawberry", "Star-Fruit"]

fruit1, fruit2, fruit3, *others = fruits # O "*others" pode ser usado no em quualquer lugar

print(fruit1)
print(fruit2)
print(fruit3)
print(others)

print()

# Enumerate (index, item) in enumerate(list)

for index ,fruit in enumerate(fruits):
    print(f"{index + 1} - {fruit}")

print()

# For value

values = [10, 50, 60, 20, 40, 66, 55, 33]

totalValues = 0

for value in values:
    totalValues += value

print(f"Your total is : ${totalValues}.")

print()

# Zip

colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]
values_for_colors = [133, 55, 817, 91, 81, 9, 138]

zip_colors_and_values = zip(colors, values_for_colors)

list_colors_and_values = list(zip_colors_and_values)

print(list_colors_and_values)

for tuple_colors in list_colors_and_values:
    print(f"Color: {tuple_colors[0]} / Price: ${tuple_colors[1]}")

print()

# Split()

input_user = input("Hi! Write yours fruits separated by commas: ")
fruits = input_user.split(",")
join_fruits = " ".join(fruits)

print(fruits)
print(join_fruits)

print()

# Map()

list1 = [10, 20, 30]

def multiply(x):
    return x * 2

list2 = list(map(multiply, list1))
print(list2)




