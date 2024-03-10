"11. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están ordenados de menor a mayor."


def numeros_ordenados(conjunto_numeros):
    # Ordena el conjunto de números de menor a mayor y lo convierte en un conjunto
    conjunto_ordenado = set(sorted(conjunto_numeros))
    # Devuelve el conjunto ordenado
    return conjunto_ordenado


# Define un conjunto de números como ejemplo
conjunto_ejemplo = {5, 2, 8, 3, 1, 7}
# Llama a la función 'numeros_ordenados' con el conjunto de ejemplo y guarda el resultado
resultado = numeros_ordenados(conjunto_ejemplo)
# Imprime el conjunto de números ordenados de menor a mayor
print("Números ordenados de menor a mayor: ", resultado)
