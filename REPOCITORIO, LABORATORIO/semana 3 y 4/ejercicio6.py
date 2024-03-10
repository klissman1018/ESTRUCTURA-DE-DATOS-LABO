"ejercicio 6: Crear una matriz de números reales"


import numpy as np  # Esta línea importa la biblioteca numpy con el alias np, lo que permite usar sus funciones y clases.

# Solicita al usuario que ingrese el número de filas y columnas de la matriz, respectivamente.
# Convierte esos valores a enteros y los almacena en las variables 'filas' y 'columnas'.
filas = int(input("Ingresa el número de filas de la matriz: "))
columnas = int(input("Ingresa el número de columnas de la matriz: "))

# Crea una matriz de ceros con dimensiones 'filas' x 'columnas'.
# El argumento 'dtype=float' especifica que los elementos de la matriz serán de tipo flotante.
matriz = np.zeros((filas, columnas), dtype=float)

# Este bucle anidado recorre cada posición de la matriz.
# 'i' representa el índice de la fila actual y 'j' el índice de la columna actual.
for i in range(filas):
    for j in range(columnas):
        # Solicita al usuario que ingrese el valor para el elemento actual de la matriz.
        # Convierte ese valor a flotante y lo asigna a la posición correspondiente en la matriz.
        matriz[i, j] = float(input(f"Ingrese el elemento [{i},{j}]: "))

# Imprime un mensaje seguido de la matriz creada.
print("La matriz creada es:")
print(matriz)
