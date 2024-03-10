" 4. Escribir una función que encuentre la submatriz de mayor suma de una matriz"

def submatriz_maxima(matriz):
    # Obtener las dimensiones de la matriz
    fila, columna = matriz.shape
    # Inicializar el valor máximo encontrado y la submatriz correspondiente
    max_val = 0
    max_submatriz = None

    # Iterar sobre cada elemento de la matriz como posible esquina superior izquierda de la submatriz
    for i in range(fila):
        for j in range(columna):
            # Asegurarse de que la submatriz de 2x2 no se salga de los límites
            if i + 1 < fila and j + 1 < columna:
                # Extraer la submatriz de 2x2
                submatriz = matriz[i : i + 2, j : j + 2]
                # Calcular la suma de los elementos de la submatriz
                suma = np.sum(submatriz)
                # Si la suma es mayor que el máximo actual, actualizar el máximo y la submatriz máxima
                if suma > max_val:
                    max_val = suma
                    max_submatriz = submatriz
    # Devolver la submatriz de mayor suma encontrada
    return max_submatriz


# Imprimir la submatriz de mayor suma de una matriz aleatoria previamente definida
print("Submatriz de mayor suma: \n", submatriz_maxima(matriz_aleatoria))
