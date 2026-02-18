import numpy as np

# Arrays usam menos bytes que listas!!!!

# ------------------- 1D -------------------------

array_1D = np.array([1,2,3,4,5])
#print(array_1D)

# .shape() mostra se a lista é 1D, 2D ou 3D
#ex. (3,) = 1D / (3, 5) = 2D / (3, 5, 3) = 3D
print(np.shape(array_1D))

# .ndim diz quantas dimensões existem nesta array
print(np.ndim(array_1D))

# Aqui diz que tipo é o valor(s) dentro da array
print(array_1D.dtype)

# -------------------- 2D --------------------------

array_2D = np.array([[1,2,3], [4,5,6]])
print(array_2D)

print(np.shape(array_2D))

print(np.ndim(array_2D))

print(array_2D.dtype)

# -------------------- 3D ---------------------------

array_3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(array_3D)

print(np.shape(array_3D))

print(np.ndim(array_3D))

print(array_3D.dtype)