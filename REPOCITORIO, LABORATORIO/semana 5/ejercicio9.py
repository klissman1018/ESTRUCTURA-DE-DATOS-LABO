"9. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que tienen una longitud determinada."


# Define una función que recibe un conjunto de palabras y una longitud deseada.
def palabras_con_longitud(conjunto_palabras, longitud_deseada):
    # Utiliza una comprensión de conjunto para seleccionar palabras que tengan la longitud deseada.
    palabras_seleccionadas = {
        palabra for palabra in conjunto_palabras if len(palabra) == longitud_deseada
    }
    # Devuelve el conjunto de palabras seleccionadas.
    return palabras_seleccionadas


# Crea un conjunto de palabras para probar la función.
conjunto_palabras = {"oso", "reconocer", "hola", "radar", "python", "civic"}
# Establece la longitud deseada de las palabras a buscar.
longitud_deseada = 4

# Llama a la función con el conjunto de palabras y la longitud deseada, y guarda el resultado.
resultado_palabras = palabras_con_longitud(conjunto_palabras, longitud_deseada)

# Imprime el resultado, mostrando las palabras que tienen la longitud deseada.
print(f"Palabras con longitud {longitud_deseada}:", resultado_palabras)
