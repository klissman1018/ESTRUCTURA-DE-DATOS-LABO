"20. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor."


def es_palindromo(palabra):
    # Compara la palabra con su versión invertida para verificar si es un palíndromo
    return palabra == palabra[::-1]


def palindromos_longitud_ordenados(conjunto_palabras, longitud):
    # Crea un conjunto de palabras que son palíndromos y tienen la longitud especificada
    palindromos_set = {
        palabra
        for palabra in conjunto_palabras
        if es_palindromo(palabra) and len(palabra) == longitud
    }
    # Ordena el conjunto de palíndromos y lo convierte en un conjunto para eliminar duplicados
    palindromos_ordenados_set = set(sorted(palindromos_set))
    # Devuelve el conjunto de palíndromos ordenados
    return palindromos_ordenados_set


# Define un conjunto de palabras de ejemplo
conjunto_ejemplo = {"level", "radar", "python", "deified", "hello"}
# Especifica la longitud deseada de las palabras
longitud_deseada = 5
# Llama a la función con el conjunto de ejemplo y la longitud deseada, y guarda el resultado
resultado = palindromos_longitud_ordenados(conjunto_ejemplo, longitud_deseada)
# Imprime los palíndromos de la longitud deseada, ordenados de menor a mayor
print(
    "Palíndromos de longitud ",
    longitud_deseada,
    "ordenados de menor a mayor: ",
    resultado,
)
