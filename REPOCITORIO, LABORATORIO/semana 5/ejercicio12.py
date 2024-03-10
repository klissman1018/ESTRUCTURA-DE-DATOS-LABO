"12. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están ordenados de mayor a menor."

# Definimos una función llamada numeros_ordenados_descendente que toma un argumento llamado conjunto_numeros.
def numeros_ordenados_descendente(conjunto_numeros):
    # Dentro de la función, creamos una variable llamada conjunto_ordenado_descendente.
    # Esta variable almacena el conjunto de números ordenados de mayor a menor.
    # Usamos la función sorted() para ordenar los números, con el argumento reverse=True para que el orden sea descendente.
    # Luego, convertimos la lista ordenada en un conjunto usando set().
    conjunto_ordenado_descendente = set(sorted(conjunto_numeros, reverse=True))
    
    # La función retorna el conjunto ordenado de manera descendente.
    return conjunto_ordenado_descendente

# Creamos un conjunto de ejemplo llamado conjunto_ejemplo con algunos números.
conjunto_ejemplo = {5, 2, 8, 3, 1, 7}
# Llamamos a la función numeros_ordenados_descendente con el conjunto_ejemplo como argumento.
# El resultado se almacena en la variable resultado.
resultado = numeros_ordenados_descendente(conjunto_ejemplo)
# Imprimimos el resultado, que son los números del conjunto ordenados de mayor a menor.
print("Números ordenados de mayor a menor: ", resultado)