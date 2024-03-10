"7. Crear una matriz de números complejos"

import numpy as np  # Importa la biblioteca numpy con el alias np

# Solicita al usuario el número de filas y columnas de la matriz y los convierte a entero
filas = int(input("Ingresa el número de filas de la matriz: "))
columnas = int(input("Ingresa el número de columnas de la matriz: "))

# Crea una matriz de ceros con dimensiones filas x columnas de tipo complejo
matriz = np.zeros((filas, columnas), dtype=complex)
# Recorre cada elemento de la matriz mediante dos bucles for anidados
for i in range(filas):
    for j in range(columnas):
        # Solicita al usuario la parte real e imaginaria de cada elemento de la matriz
        real = float(input(f"Ingrese la parte real del elemento [{i},{j}]: "))
        imag = float(input(f"Ingrese la parte imaginaria del elemento [{i},{j}]: "))
        # Asigna el valor complejo a la posición correspondiente en la matriz
        matriz[i, j] = complex(real, imag)

# Imprime la matriz creada
print("La matriz creada es:")
print(matriz)
