"7. Asegurar que un función retorna un valoe específico"

def calcular_area_rectangulo(largo, ancho):
    assert largo > 0 and ancho > 0, "El largo y el ancho deben ser positivos"
    return largo * ancho

# Ejemplo de uso:
try:
    area = calcular_area_rectangulo(
        5, 3
    )  # Esto es válido y no se lanzará ninguna excepción
    print(area)  # Imprimirá  15
    area = calcular_area_rectangulo(-5, 3)  # Esto lanzará un AssertionError
except AssertionError as e:
    print(e)  # Imprimirá "El largo y el ancho deben ser positivos"
