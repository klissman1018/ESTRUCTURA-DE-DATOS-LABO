"3. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que son divisibles por un número determinado."


def numeros_divisibles_por(conjunto, divisor):
    # Utiliza una comprensión de conjunto para filtrar los números divisibles por 'divisor'
    return {numero for numero in conjunto if numero % divisor == 0}


# Define un conjunto de números del 1 al 10
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Establece el número por el cual se desea verificar la divisibilidad
divisor = 2

# Llama a la función 'numeros_divisibles_por' con el conjunto y el divisor definidos anteriormente
resultado = numeros_divisibles_por(conjunto, divisor)

# Imprime el resultado de la función, mostrando los números divisibles por el divisor
print(f"Números divisibles por {divisor}:", resultado)
