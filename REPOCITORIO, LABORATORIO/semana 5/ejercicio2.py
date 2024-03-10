"2. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que comienzan con una letra determinada."

# Define una función llamada palabrasinicial que toma un conjunto de palabras como argumento
def palabrasinicial(conjunto_palabras):
    # Retorna un nuevo conjunto compuesto por aquellas palabras del conjunto de entrada que comienzan con la letra "c"
    # Esto se logra mediante una comprensión de conjunto que itera sobre cada palabra en conjunto_palabras
    # y selecciona solo aquellas que cumplen con la condición palabra.startswith("c")
    return {palabra for palabra in conjunto_palabras if palabra.startswith("c")}


# Crea un conjunto de palabras para ser utilizado como ejemplo
conjunto_palabras = {"casa", "zapato", "auto", "cienpies", "laptop"}

# Llama a la función palabrasinicial pasándole el conjunto de palabras creado anteriormente
# y almacena el resultado en la variable resultado
resultado = palabrasinicial(conjunto_palabras)
# Imprime el conjunto de palabras que comienzan con la letra "c", contenido en la variable resultado
print("Palabras que comienzan con 'c':", resultado)
