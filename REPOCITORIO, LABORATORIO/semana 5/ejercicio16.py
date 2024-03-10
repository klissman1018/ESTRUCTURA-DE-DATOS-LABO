"16. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos y están ordenadas de menor a mayor."


def es_primo(numero):
    # Si el número es menor que 2, no puede ser primo
    if numero < 2:
        return False
    # Itera desde 2 hasta la raíz cuadrada del número + 1
    for i in range(2, int(numero**0.5) + 1):
        # Si el número es divisible por i, entonces no es primo
        if numero % i == 0:
            return False
    # Si no se encontraron divisores, el número es primo
    return True


def primos_ordenados(conjunto_numeros):
    # Crea un conjunto de números primos filtrando el conjunto original
    primos_set = {numero for numero in conjunto_numeros if es_primo(numero)}
    # Ordena el conjunto de números primos y lo convierte en un conjunto
    primos_ordenados_set = set(sorted(primos_set))
    # Devuelve el conjunto ordenado de números primos
    return primos_ordenados_set


# Define un conjunto de números como ejemplo
conjunto_ejemplo = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Llama a la función y guarda el resultado
resultado = primos_ordenados(conjunto_ejemplo)
# Imprime el conjunto de números primos ordenados de menor a mayor
print("Números primos ordenados de menor a mayor: ", resultado)


def es_palindromo(palabra):
    # Comprueba si la palabra es igual a su inversa
    return palabra == palabra[::-1]


def palindromos_ordenados(conjunto_palabras):
    # Crea un conjunto de palabras que son palíndromos
    palindromos_set = {
        palabra for palabra in conjunto_palabras if es_palindromo(palabra)
    }
    # Ordena el conjunto de palíndromos y lo convierte en un conjunto
    palindromos_ordenados_set = set(sorted(palindromos_set))
    # Devuelve el conjunto ordenado de palíndromos
    return palindromos_ordenados_set


# Define un conjunto de palabras como ejemplo
conjunto_ejemplo = {"radar", "python", "level", "Scratch", "Java"}
# Llama a la función y guarda el resultado
resultado = palindromos_ordenados(conjunto_ejemplo)
# Imprime el conjunto de palíndromos ordenados de menor a mayor
print("Palíndromos ordenados de menor a mayor: ", resultado)
