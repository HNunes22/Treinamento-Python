import numpy as np

array_a = np.array([1, 2 ,3, 4, 5])
array_b = np.array([1, 2, 3, 4, 5])

# Irá somar os valores das listas, as arrays precisam ter o mesmo tamanho ou irá gerar um erro

# ex. array_a[0] + array_b[0] = 2.
print(np.add(array_a, array_b))