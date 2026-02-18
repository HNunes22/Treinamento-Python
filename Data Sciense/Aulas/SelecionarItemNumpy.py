import numpy as np

array_a = np.array([[1, 2, 3], [4, 5, 6]])

# Sintex: array[row, column]

print(array_a[1, 1]) # = 5

# Sintex: array[row, :], : significa "Quero todas as colunas.
print(array_a[1,:])

# Sintex: array[:, column]
print(array_a[:,2])