# Sets

numbers1 =  [1, 2, 3, 11, 12, 4]
numbers2 = [4, 5, 6, 7, 8, 9, 10, 11, 12]

# Converter para sets, ele irá perder a index

num1  = set(numbers1)
num2 = set(numbers2)

print(num1 | num2) # Unir as sets (removendo iguais)

print(num1 - num2) # Exibe os valores defirentes comparando as listas

print(num1 ^ num2) # Mostrar os valores que não se repetem nas listas

print(num1 & num2)  # Mostrar o que tem  de igual nas listas

print()
# Funcs

set_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

# Add

set_numbers.add(13)
print(set_numbers)

# Update

set_numbers.update([12, 13, 14, 15, 16, 17])
print(set_numbers)

# Discard

set_numbers.discard(4)
print(set_numbers)

print()

# Funcs (string)

set_chars = {'a', 'b', 'c'}
set_chars_2 = {'d', 'b', 'a'}
set_chars_3 = {'f', 'g', 'c'}

# Union() Unir os sets

set_chars_4 = set_chars.union(set_chars_2)
print(set_chars)

# Difference() Ver o valor diferente

set_chars_5 = set_chars_2.difference(set_chars)
print(set_chars_5)

# Intersection() O que tem de igual

set_chars_6 = set_chars_3.intersection(set_chars)
print(set_chars_6)