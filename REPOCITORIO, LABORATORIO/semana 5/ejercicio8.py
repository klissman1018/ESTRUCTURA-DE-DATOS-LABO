"8. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos."


def palindromo(palabra):
    # Compara la palabra con su versión invertida para verificar si es un palíndromo
    return palabra == palabra[::-1]  # palabra[::-1] invierte la palabra


def palindromos_en_conjunto(conjunto_palabras):
    # Crea un conjunto de palabras que son palíndromos usando comprensión de conjuntos
    palindromos = {
        palabra for palabra in conjunto_palabras if palindromo(palabra)
    }  # Filtra solo los palíndromos
    return palindromos  # Devuelve el conjunto de palíndromos


# Define un conjunto de palabras para buscar palíndromos
conjunto_palabras = {"oso", "reconocer", "hola", "radar", "python", "civic"}

# Llama a la función palindromos_en_conjunto y guarda el resultado
resultado_palindromos = palindromos_en_conjunto(conjunto_palabras)

# Imprime el conjunto de palabras que son palíndromos
print("Conjunto de palíndromos:", resultado_palindromos)
