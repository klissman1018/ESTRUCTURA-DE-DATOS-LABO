"5. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están en el primer conjunto pero no en el segundo."

def diferenciadeconjuntos1(conjunto1, conjunto2):
    # Convierte el primer conjunto de entrada en un conjunto de Python para asegurar la unicidad de elementos
    conjunto1 = set(conjunto1)
    # Convierte el segundo conjunto de entrada en un conjunto de Python para asegurar la unicidad de elementos
    conjunto2 = set(conjunto2)

    # Calcula la diferencia entre el primer y segundo conjunto, es decir, los elementos que están en el primero pero no en el segundo
    diferencia = conjunto1 - conjunto2

    # Retorna el conjunto resultante de la diferencia
    return diferencia


# Define el primer conjunto de números
conjunto_a = {1, 2, 3, 4, 5}
# Define el segundo conjunto de números
conjunto_b = {3, 4, 5, 6, 7}

# Llama a la función diferenciadeconjuntos1 con los conjuntos definidos anteriormente y guarda el resultado
resultado = diferenciadeconjuntos1(conjunto_a, conjunto_b)

# Imprime el conjunto resultante de la diferencia
print("Conjunto resultante:", resultado)
