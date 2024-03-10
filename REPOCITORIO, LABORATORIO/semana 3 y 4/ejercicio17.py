"5. Escribir una función que encuentre la matriz de covarianza de dos matrices:"

# Definición de la función para calcular la matriz de covarianza entre dos matrices
def matriz_covarianza(matriz1, matriz2):
    # Utiliza la función cov de numpy para calcular la matriz de covarianza y la retorna
    return np.cov(matriz1, matriz2)


# Genera una matriz de 100x100 con valores aleatorios para el ejemplo
matriz1 = np.random.rand(100, 100)
# Genera otra matriz de 100x100 con valores aleatorios para el ejemplo
matriz2 = np.random.rand(100, 100)

# Imprime la matriz de covarianza calculada entre las dos matrices anteriores
print("Matriz de covarianza: \n", matriz_covarianza(matriz1, matriz2))
