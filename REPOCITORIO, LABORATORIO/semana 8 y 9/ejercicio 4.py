"4 Asegurar que una lista no esté vacía."


# Se crea una lista llamada 'mi_lista' y se inicializa con tres elementos: 1, 2, y 3.
mi_lista = [1, 2, 3]

# Se utiliza una estructura condicional 'if' para verificar si la longitud de 'mi_lista' es mayor que 0.
if len(mi_lista) > 0:
    # Si la condición es verdadera, significa que 'mi_lista' tiene al menos un elemento y no está vacía.
    # Por lo tanto, se imprime el mensaje "La lista no está vacía."
    print("La lista no está vacía.")
else:
    # Si la condición es falsa, significa que 'mi_lista' no tiene elementos y está vacía.
    # Por lo tanto, se imprime el mensaje "La lista está vacía."
    print("La lista está vacía.")
