"11. Multiplicar una matriz por un número"

import numpy as np

# Definir la matriz
matriz = np.array([[1, 2], [3, 4]])

# Definir el número por el cual se multiplicará la matriz
numero = 3

# Multiplicar la matriz por el número
resultado = matriz * numero

print("Matriz original:")
print(matriz)

print("Matriz multiplicada por", numero, ":")
print(resultado)
