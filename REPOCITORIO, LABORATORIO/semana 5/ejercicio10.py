"10. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que contienen una letra determinada."


def palabras_con_letra(conjunto_palabras, letra_deseada):
    # Esta función recibe un conjunto de palabras y una letra deseada.
    # Su objetivo es encontrar todas las palabras en el conjunto que contengan la letra deseada.
    
    palabras_seleccionadas = {
        palabra  # Para cada palabra en el conjunto de palabras,
        for palabra in conjunto_palabras  # se itera sobre cada palabra.
        if letra_deseada
        in palabra  # Si la letra deseada está en la palabra,
    }  # esa palabra se agrega al conjunto palabras_seleccionadas.
    return palabras_seleccionadas  # La función devuelve el conjunto de palabras seleccionadas.

conjunto_palabras = {"oso", "reconocer", "hola", "radar", "python", "civic"}
# Se define un conjunto de palabras para buscar aquellas que contengan una letra específica.

letra_deseada = "o"
# Se define la letra que se desea buscar en el conjunto de palabras.

resultado_palabras = palabras_con_letra(conjunto_palabras, letra_deseada)
# Se llama a la función palabras_con_letra con el conjunto de palabras y la letra deseada,
# y se guarda el resultado en resultado_palabras.

print(f"Palabras que contienen la letra '{letra_deseada}':", resultado_palabras)
# Se imprime el conjunto de palabras que contienen la letra deseada.
