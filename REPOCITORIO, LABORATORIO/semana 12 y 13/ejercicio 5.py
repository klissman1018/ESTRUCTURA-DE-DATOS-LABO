#Ejercicios parte 02 - Arboles:
#Contar nodos:
#5.    Implementar una función que cuente la cantidad de nodos en el árbol.

def contar_nodos(nodo):
    # Define una función llamada contar_nodos, la cual toma un argumento llamado 'nodo'.
    # Esta función tiene como objetivo contar el número total de nodos en un árbol.
    
    # Comprueba si el nodo actual es None (nulo), lo que indica un nodo vacío.
    if nodo is None:
        # Si el nodo es None, retorna 0 ya que no hay nodos que contar.
        return 0
    else:
        # Si el nodo no es None, inicia el conteo con 1, contando el nodo actual.
        total = 1
        # Itera sobre cada uno de los hijos del nodo actual, si los tiene.
        # Utiliza el método .get() para obtener la lista de hijos del nodo,
        # si no tiene hijos, utiliza una lista vacía como valor por defecto.
        for hijo in nodo.get('hijos', []):
            # Por cada hijo del nodo, llama recursivamente a la función contar_nodos.
            # Esto permite contar todos los nodos en los subárboles del nodo actual.
            # Suma el resultado de la llamada recursiva al total de nodos.
            total += contar_nodos(hijo)
        # Después de iterar sobre todos los hijos y contar todos los nodos,
        # retorna el número total de nodos.
        return total

# Crea un diccionario que representa un árbol. El árbol tiene un nodo raíz 'A'
# y varios hijos y nietos, representados en una estructura anidada.
arbol = {
    'valor': 'A',
    'hijos': [
        {'valor': 'B', 'hijos': [{'valor': 'D'}]},
        {'valor': 'C', 'hijos': [{'valor': 'E'}, {'valor': 'F'}]}
    ]
}

# Llama a la función contar_nodos, pasando el árbol definido anteriormente como argumento.
# Esto inicia el proceso de contar todos los nodos en el árbol.
cantidad_nodos = contar_nodos(arbol)
# Imprime el resultado, mostrando el número total de nodos en el árbol.
print(f"El árbol tiene {cantidad_nodos} nodos.")
