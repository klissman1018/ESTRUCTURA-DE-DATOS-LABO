"5. Validar la igualdad de dos objetos."


def validar_igualdad(objeto1, objeto2):
    # Utiliza la declaración assert para verificar si objeto1 es igual a objeto2
    assert (
        objeto1 == objeto2
    ), "Los objetos no son iguales"  # Si no son iguales, lanza una excepción con el mensaje "Los objetos no son iguales"
    print(
        "Los objetos son iguales."
    )  # Si son iguales, imprime "Los objetos son iguales."


# Intenta ejecutar el bloque de código siguiente
try:
    validar_igualdad(
        10, 10
    )  # Llama a la función validar_igualdad con dos números iguales
    validar_igualdad(
        "Hola", "Hola"
    )  # Llama a la función validar_igualdad con dos cadenas de texto iguales
    validar_igualdad(
        "Hola", "Adiós"
    )  # Llama a la función validar_igualdad con dos cadenas de texto diferentes
# Captura la excepción AssertionError si se lanza en el bloque try
except AssertionError as e:
    print(e)  # Imprime el mensaje de error asociado a la excepción
