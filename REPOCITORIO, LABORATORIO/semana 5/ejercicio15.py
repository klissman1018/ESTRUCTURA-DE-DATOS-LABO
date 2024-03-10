"15. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que son primos y están ordenados de menor a mayor."


def es_primo(numero):
    # Si el número es menor que 2, no es primo
    if numero < 2:
        return False
    # Comprueba si el número es divisible por algún número hasta su raíz cuadrada
    for i in range(2, int(numero**0.5) + 1):
        # Si el número es divisible por i, no es primo
        if numero % i == 0:
            return False
    # Si el número no es divisible por ningún número en el rango, es primo
    return True


def primos_ordenados(conjunto_numeros):
    # Crea un conjunto de números primos a partir del conjunto de entrada
    primos_set = {numero for numero in conjunto_numeros if es_primo(numero)}
    # Ordena el conjunto de números primos y lo convierte en un conjunto
    primos_ordenados_set = set(sorted(primos_set))
    # Devuelve el conjunto de números primos ordenados
    return primos_ordenados_set


# Define un conjunto de números como ejemplo
conjunto_ejemplo = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Llama a la función 'primos_ordenados' con el conjunto de ejemplo y guarda el resultado
resultado = primos_ordenados(conjunto_ejemplo)
# Imprime el conjunto de números primos ordenados de menor a mayor
print("Números primos ordenados de menor a mayor: ", resultado)
