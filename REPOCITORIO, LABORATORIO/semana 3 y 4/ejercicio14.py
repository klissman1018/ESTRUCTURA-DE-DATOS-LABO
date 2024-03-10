"2 Calcular la desviación estándar de los elementos de la matriz"

import numpy as np  # Esta línea importa la biblioteca numpy con el alias 'np', permitiendo el uso de sus funciones y métodos.

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Crea una matriz 3x3 utilizando la función array de numpy.

desviacion_estandar = np.std(matriz)  # Calcula la desviación estándar de todos los elementos de la matriz.

print("La desviación estándar de los elementos de la matriz es:", desviacion_estandar)  # Imprime el valor de la desviación estándar calculada.
