"3. Validar el rango de una calificación."


# Define una función para validar una calificación
def validar_calificacion(calificacion):
    # Asegura que la calificación esté en el rango de 0 a 100, si no, lanza una excepción con un mensaje
    assert 0 <= calificacion <= 100, "La calificación debe estar entre  0 y  100"
    # Si la calificación es válida, imprime un mensaje de confirmación
    print("La calificación es válida.")


# Bloque de código que intenta ejecutar las validaciones de calificaciones
try:
    # Llama a la función validar_calificacion con una calificación válida (90)
    validar_calificacion(90)
    # Llama a la función validar_calificacion con una calificación inválida (110) para probar la excepción
    validar_calificacion(110)
# Captura la excepción AssertionError si alguna calificación no cumple con el rango válido
except AssertionError as e:
    # Imprime el mensaje de error asociado a la excepción capturada
    print(e)
