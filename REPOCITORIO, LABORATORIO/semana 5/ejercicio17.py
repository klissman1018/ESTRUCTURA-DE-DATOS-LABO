"17. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que tienen una longitud determinada y están ordenadas de menor a mayor"


def palabras_longitud_ordenadas(conjunto_palabras, longitud):
    # Crea un conjunto con las palabras que tienen la longitud especificada
    palabras_f = {palabra for palabra in conjunto_palabras if len(palabra) == longitud}
    # Ordena el conjunto de palabras filtradas y lo convierte de nuevo en un conjunto
    palabras_ordenadas_set = set(sorted(palabras_f))
    # Devuelve el conjunto de palabras ordenadas
    return palabras_ordenadas_set


# Define un conjunto de palabras como ejemplo
conjunto_ejemplo = {"python", "java", "shard", "javascript", "level"}
# Especifica la longitud deseada de las palabras
longitud_deseada = 5
# Llama a la función y guarda el resultado en una variable
resultado = palabras_longitud_ordenadas(conjunto_ejemplo, longitud_deseada)
# Imprime las palabras que cumplen con la longitud deseada, ordenadas de menor a mayor
print(
    "Palabras de longitud ", longitud_deseada, "ordenadas de menor a mayor: ", resultado
)
