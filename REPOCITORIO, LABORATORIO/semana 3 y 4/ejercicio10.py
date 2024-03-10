"10. Suma de dos matrices de diferentes tamaños"


# Se crea una matriz llamada matriz1 utilizando la función array de numpy con los elementos especificados
matriz1 = np.array(
    [
        [
            1,
            2,
        ],
        [3, 4],
    ]
)
# Se crea una segunda matriz llamada matriz2 utilizando la función array de numpy con los elementos especificados
matriz2 = np.array([[5, 6], [7, 8]])
# Se suman las dos matrices anteriores y el resultado se almacena en la variable suma_matrices
suma_matrices = matriz1 + matriz2
# Se imprime el resultado de la suma de las dos matrices
print("suma de matrices de diferentes tamaños: ", suma_matrices)
