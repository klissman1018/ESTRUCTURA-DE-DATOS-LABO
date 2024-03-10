"9. Asegurar que un módulo se ha importado correctamente."


# Importar el módulo sys
import sys

# Definir la función importar_modulo que recibe el nombre del módulo a importar
def importar_modulo(nombre_modulo):
    # Intentar importar el módulo dado
    try:
        __import__(nombre_modulo)
    # Capturar la excepción ModuleNotFoundError en caso de que el módulo no exista
    except ModuleNotFoundError as e:
        # Imprimir un mensaje de error indicando el módulo que falló en importarse
        print(f"Error al importar el módulo {nombre_modulo}: {e}")
        return False

    # Verificar que el módulo importado está en sys.modules
    assert (
        nombre_modulo in sys.modules
    ), f"El módulo {nombre_modulo} no se ha importado correctamente."
    # Imprimir un mensaje indicando que el módulo se ha importado correctamente
    print(f"El módulo {nombre_modulo} se ha importado correctamente.")
    return True


# Ejemplo de uso:
# Importar el módulo "hashlib" y mostrar un mensaje de éxito
importar_modulo(
    "hashlib"
)  # Esto imprimirá "El módulo hashlib se ha importado correctamente."
# Intentar importar un módulo inexistente y mostrar un mensaje de error
importar_modulo(
    "modulo_inexistente"
)  # Esto imprimirá un error y "El módulo modulo_inexistente no se ha importado correctamente."
