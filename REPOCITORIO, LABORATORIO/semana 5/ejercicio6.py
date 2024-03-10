"6. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están en el segundo conjunto pero no en el primero."


# Define una función para calcular la diferencia entre dos conjuntos
def diferenciadeconjuntos2(conjunto1, conjunto2):
    # Convierte el primer argumento en un conjunto para asegurar la unicidad de sus elementos
    conjunto1 = set(conjunto1)
    # Convierte el segundo argumento en un conjunto para asegurar la unicidad de sus elementos
    conjunto2 = set(conjunto2)
    # Calcula la diferencia de conjuntos, es decir, los elementos que están en conjunto2 pero no en conjunto1
    diferencia = conjunto2 - conjunto1
    # Retorna el conjunto resultante de la diferencia
    return diferencia


# Define el primer conjunto de números para la operación
conjunto_a = {1, 2, 3, 4, 5}
# Define el segundo conjunto de números para la operación
conjunto_b = {3, 4, 5, 6, 7}
# Llama a la función 'diferenciadeconjuntos2' con los dos conjuntos definidos y guarda el resultado en 'resultado'
resultado = diferenciadeconjuntos2(conjunto_a, conjunto_b)
# Imprime el conjunto resultante de la diferencia de los dos conjuntos
print("Conjunto resultante:", resultado)
