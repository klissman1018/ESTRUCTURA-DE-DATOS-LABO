"19. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están ordenados de menor a mayor y que no están duplicados." 


def numeros_ordenados_sin_duplicados(conjunto_numeros):
    # Ordena el conjunto de números y elimina duplicados convirtiéndolo en un conjunto
    numeros_ordenados_set = set(sorted(conjunto_numeros))
    # Devuelve el conjunto de números ordenados y sin duplicados
    return numeros_ordenados_set


# Define un conjunto de números como ejemplo, incluyendo duplicados
conjunto_ejemplo = {5, 2, 8, 3, 1, 7, 2, 8}
# Llama a la función y guarda el resultado en la variable 'resultado'
resultado = numeros_ordenados_sin_duplicados(conjunto_ejemplo)
# Imprime el resultado, mostrando los números ordenados de menor a mayor sin duplicados
print("Números ordenados de menor a mayor sin duplicados: ", resultado)
