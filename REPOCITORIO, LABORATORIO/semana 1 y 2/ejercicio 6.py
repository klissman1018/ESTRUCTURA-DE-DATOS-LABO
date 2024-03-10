"6. Toma una cadena de texto y muestra su inversión."

# Definimos una función llamada invertir_cadena que acepta un parámetro llamado cadena
def invertir_cadena(cadena):
    # La función devuelve la cadena recibida pero invertida, gracias al uso de slicing [::-1]
    return cadena[::-1]

# Creamos una variable texto_inicial y le asignamos el valor de la cadena "buenos dias"
texto_inicial = "buenos dias"
# Llamamos a la función invertir_cadena pasándole como argumento la variable texto_inicial y guardamos el resultado en texto_invertido
texto_invertido = invertir_cadena(texto_inicial)

# Imprimimos en consola la cadena "texto inicial :" seguido del valor de la variable texto_inicial
print("texto inicial :", texto_inicial)
# Imprimimos en consola la cadena "texto invertir:" seguido del valor de la variable texto_invertido
print("texto invertir:",texto_invertido)