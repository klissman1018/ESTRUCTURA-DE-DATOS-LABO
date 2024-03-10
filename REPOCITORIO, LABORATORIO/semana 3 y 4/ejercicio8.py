"8. Crear una matriz de matrices"


# Solicitar al usuario las dimensiones de la matriz
filas = int(input("Ingresa el número de filas de la matriz de matrices: "))
columnas = int(input("Ingresa el número de columnas de la matriz de matrices: "))

# Inicializar una matriz de matrices vacía con las dimensiones especificadas por el usuario
matriz_de_matrices = np.empty(
    (filas, columnas), dtype=object
)  # Crea una matriz vacía para almacenar submatrices
for i in range(filas):  # Iterar sobre cada fila de la matriz principal
    for j in range(columnas):  # Iterar sobre cada columna de la matriz principal
        # Solicitar al usuario las dimensiones de cada submatriz
        sub_filas = int(
            input(f"Ingrese el número de filas de la submatriz [{i},{j}]: ")
        )  # Guarda el número de filas de la submatriz actual
        sub_columnas = int(
            input(f"Ingrese el número de columnas de la submatriz [{i},{j}]: ")
        )  # Guarda el número de columnas de la submatriz actual
        # Crear y asignar una submatriz de ceros con las dimensiones especificadas por el usuario
        matriz_de_matrices[i, j] = np.zeros(
            (sub_filas, sub_columnas)
        )  # Asigna una submatriz de ceros a la posición actual en la matriz principal

# Mostrar la matriz de matrices completa
print("La matriz de matrices creada es:")  # Imprime un mensaje indicativo
print(matriz_de_matrices)  # Imprime la matriz de matrices completa
