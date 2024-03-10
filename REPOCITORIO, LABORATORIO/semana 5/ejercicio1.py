"PARTE 1°"
"1. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números primos"

def num_primo(primo):
    # Si el número es 1, no es primo, retorna Falso
    if primo == 1:
        return False
    # Itera desde 2 hasta la raíz cuadrada del número + 1
    for i in range(2, int(primo**0.5) + 1):
        # Si el número es divisible por i, no es primo, retorna Falso
        if primo % i == 0:
            return False
    # Si no se encontraron divisores, el número es primo, retorna Verdadero
    return True

def conjuntos_primos(conjunto):
    # Crea un conjunto de números primos filtrando aquellos que son primos en el conjunto dado
    primos = {numero for numero in conjunto_numeros if num_primo(numero)}
    # Retorna el conjunto de números primos
    return primos

# Define un conjunto de números
conjunto_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

# Llama a la función conjuntos_primos y guarda el resultado en resultado_primos
resultado_primos = conjuntos_primos(conjunto_numeros)

# Imprime los números primos encontrados en el conjunto
print("Números primos en el conjunto:", resultado_primos)
