"9.  Acceder al elemento central de una matriz"


import numpy as np

# Crear una matriz de ejemplo
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Obtener el número de filas y columnas de la matriz
filas, columnas = matriz.shape

# Calcular el índice del elemento central
indice_central_fila = filas // 2
indice_central_columna = columnas // 2

# Acceder al elemento central
elemento_central = matriz[indice_central_fila, indice_central_columna]

print("El elemento central de la matriz es:", elemento_central)
