"3. Escribir una función que encuentre el elemento máximo de una matriz"


import numpy as np  # Importa la biblioteca numpy con el alias np para realizar operaciones matemáticas avanzadas.

def encontrar_maximo(matriz):
    # Define una función llamada encontrar_maximo que toma un argumento llamado matriz.
    maximo = np.max(matriz)  # Utiliza la función max de numpy para encontrar el valor máximo en la matriz proporcionada.
    return maximo  # Devuelve el valor máximo encontrado en la matriz.

matriz = np.array([[1, 2, 3], [4, 9, 6], [7, 8, 5]])  # Crea una matriz numpy a partir de una lista de listas.

maximo = encontrar_maximo(matriz)  # Llama a la función encontrar_maximo con la matriz creada y almacena el resultado en maximo.

print("El elemento máximo de la matriz es:", maximo)  # Imprime el valor máximo encontrado en la matriz.
