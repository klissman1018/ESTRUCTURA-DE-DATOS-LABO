"7. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son anagramas."


def anagramas(palabra1, palabra2):
    # Ordena alfabéticamente los caracteres de cada palabra y compara si son iguales, lo que indica que son anagramas.
    return sorted(palabra1) == sorted(palabra2)


def anagramas_conjunto(conjunto_palabras):
    # Convierte el conjunto de palabras en una lista para poder iterar sobre ella.
    lista_palabras = list(conjunto_palabras)
    # Inicializa un conjunto vacío para almacenar el resultado.
    resultado = set()

    # Itera sobre cada palabra en la lista de palabras.
    for i in range(len(lista_palabras)):
        # Itera sobre las palabras siguientes a la palabra actual para evitar comparaciones repetidas.
        for j in range(i + 1, len(lista_palabras)):
            # Asigna la palabra actual y la siguiente a variables para mejorar la legibilidad.
            primera = lista_palabras[i]
            segunda = lista_palabras[j]

            # Comprueba si las dos palabras seleccionadas son anagramas.
            if anagramas(primera, segunda):
                # Si son anagramas, añade ambas palabras al conjunto de resultado.
                resultado.add(primera)
                resultado.add(segunda)

    # Devuelve el conjunto de palabras que son anagramas entre sí.
    return resultado


# Define un conjunto de palabras para buscar anagramas.
conjunto_palabras = {"roma", "amor", "perro", "rrope", "alcohol", "gato"}

# Llama a la función anagramas_conjunto con el conjunto de palabras definido y almacena el resultado.
resultanagramas = anagramas_conjunto(conjunto_palabras)

# Imprime el conjunto de palabras que son anagramas.
print("Conjunto de anagramas:", resultanagramas)
