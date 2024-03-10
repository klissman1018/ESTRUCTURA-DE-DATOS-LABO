"9. Cuenta el número de vocales en una cadena de texto."

def contar_vocales(cadena):
    # Inicializa un contador en 0 para llevar la cuenta de las vocales
    contador = 0
    # Itera sobre cada caracter en la cadena de texto proporcionada
    for caracter in cadena:
        # Convierte el caracter actual a minúscula para hacer la comparación insensible a mayúsculas
        caracter = caracter.lower()
        # Verifica si el caracter actual es una vocal
        if caracter in 'aeiou':
            # Si es una vocal, incrementa el contador en 1
            contador += 1
    # Devuelve el número total de vocales encontradas en la cadena
    return contador

# Solicita al usuario que ingrese una cadena de texto
texto = input("Ingrese una cadena de texto: ")
# Llama a la función contar_vocales con el texto ingresado y almacena el resultado en cantidad_vocales
cantidad_vocales = contar_vocales(texto)
# Imprime el número de vocales encontradas en el texto ingresado
print(f"El número de vocales en '{texto}' es: {cantidad_vocales}")