"18. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que contienen una letra determinada y están ordenadas de mayor a menor."


def palabras_con_letra_ordenadas(conjunto_palabras, letra):
    # Crea un conjunto con las palabras que contienen la letra especificada
    palabras_filtradas = {palabra for palabra in conjunto_palabras if letra in palabra}
    # Ordena el conjunto de palabras filtradas en orden descendente y lo convierte en un conjunto
    palabras_ordenadas_set = set(sorted(palabras_filtradas, reverse=True))
    # Devuelve el conjunto de palabras ordenadas
    return palabras_ordenadas_set


# Define un conjunto de ejemplo con varias palabras
conjunto_ejemplo = {"python", "java", "shard", "javascript", "level"}
# Especifica la letra a buscar dentro de las palabras
letra_deseada = "a"
# Llama a la función con el conjunto de ejemplo y la letra deseada, y guarda el resultado
resultado = palabras_con_letra_ordenadas(conjunto_ejemplo, letra_deseada)
# Imprime las palabras que contienen la letra deseada, ordenadas de mayor a menor
print(
    "Palabras con la letra ", letra_deseada, " ordenadas de mayor a menor: ", resultado
)
