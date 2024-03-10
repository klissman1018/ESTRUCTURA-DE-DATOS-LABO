"4. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están en ambos conjuntos"

def interseccion_entre_conjuntos(conjunto1, conjunto2):
    # Convierte el primer conjunto de entrada en un conjunto de Python para asegurar la unicidad de sus elementos
    conjunto1 = set(conjunto1)
    # Convierte el segundo conjunto de entrada en un conjunto de Python para asegurar la unicidad de sus elementos
    conjunto2 = set(conjunto2)

    # Encuentra la intersección de los dos conjuntos, es decir, los elementos que están presentes en ambos conjuntos
    interseccion = conjunto1.intersection(conjunto2)

    # Devuelve el conjunto resultante de la intersección
    return interseccion


# Define el primer conjunto de números para la operación
conjunto_a = {1, 2, 3, 4, 5}
# Define el segundo conjunto de números para la operación
conjunto_b = {3, 4, 5, 6, 7}

# Llama a la función 'interseccion_entre_conjuntos' con los dos conjuntos definidos y guarda el resultado en 'resultado'
resultado = interseccion_entre_conjuntos(conjunto_a, conjunto_b)

# Imprime el conjunto resultante de la intersección de los dos conjuntos
print("Conjunto resultante:", resultado)
