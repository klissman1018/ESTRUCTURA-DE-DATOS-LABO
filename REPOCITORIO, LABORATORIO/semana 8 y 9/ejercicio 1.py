"1. Validar la edad de un usuario."


import getpass  # Importa el módulo getpass para ocultar la entrada del usuario.

def validar_edad():
    edad_str = getpass.getpass(
        "Ingrese su edad: "
    )  # Solicita al usuario su edad de manera oculta y la guarda como cadena de texto.
    try:
        edad = int(edad_str)  # Intenta convertir la cadena de texto a un entero.
        assert (
            edad >= 18
        ), "La edad debe ser mayor o igual a  18"  # Verifica que la edad sea mayor o igual a 18, si no, lanza una excepción.
        print(
            "La edad es válida."
        )  # Si la edad es mayor o igual a 18, imprime que la edad es válida.
    except (
        ValueError
    ):  # Captura la excepción si la conversión de cadena a entero falla.
        print(
            "Por favor, ingrese un número válido."
        )  # Imprime un mensaje solicitando un número válido si se captura una excepción ValueError.
    except AssertionError as e:  # Captura la excepción si la edad es menor a 18.
        print(e)  # Imprime el mensaje de error asociado a la excepción AssertionError.


# Ejemplo de uso:
validar_edad()  # Llama a la función validar_edad para ejecutar el código.
