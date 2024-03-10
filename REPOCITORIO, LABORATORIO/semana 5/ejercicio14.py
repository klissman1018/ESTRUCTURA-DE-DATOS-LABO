"14. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que no están duplicados"


def numeros_no_duplicados(conjunto_numeros):
    numeros_set = set()  # Inicializa un conjunto vacío para almacenar números únicos
    duplicados_set = (
        set()
    )  # Inicializa otro conjunto vacío para almacenar números duplicados

    for numero in conjunto_numeros:  # Itera sobre cada número en el conjunto de entrada
        if (
            numero in numeros_set
        ):  # Verifica si el número ya está en el conjunto de números únicos
            duplicados_set.add(numero)  # Si es así, lo añade al conjunto de duplicados
        else:
            numeros_set.add(numero)  # Si no, lo añade al conjunto de números únicos

    numeros_no_duplicados_set = (
        numeros_set - duplicados_set
    )  # Crea un conjunto con los números no duplicados
    return numeros_no_duplicados_set  # Devuelve el conjunto de números no duplicados


conjunto_ejemplo = {1, 2, 3, 2, 4, 5, 3, 6}  # Define un conjunto de ejemplo
resultado = numeros_no_duplicados(
    conjunto_ejemplo
)  # Llama a la función y guarda el resultado
print("Números no duplicados en el conjunto: ", resultado)  # Imprime el resultado
