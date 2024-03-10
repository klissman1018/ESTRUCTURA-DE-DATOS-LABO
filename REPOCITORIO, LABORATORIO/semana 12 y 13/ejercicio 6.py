#6.    Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos).

# Definimos una función para contar los nodos hoja de un árbol
def contar_nodos_hoja(nodo):
    # Si el nodo actual es None, significa que hemos llegado a un punto sin nodo, retornamos 0
    if nodo is None:
        return 0
    # Si el nodo actual no tiene hijos, es un nodo hoja, retornamos 1
    elif not nodo.get('hijos', []): 
        return 1
    else:
        # Inicializamos un contador de nodos hoja en 0
        total = 0
        # Iteramos sobre cada hijo del nodo actual
        for hijo in nodo.get('hijos', []):
            # Sumamos al contador el resultado de contar_nodos_hoja recursivamente para cada hijo
            total += contar_nodos_hoja(hijo)
        # Retornamos el total de nodos hoja encontrados
        return total

# Creamos un diccionario que representa nuestro árbol con un nodo raíz y sus hijos
arbol = {
    'valor': 'A',
    'hijos': [
        {'valor': 'B', 'hijos': [{'valor': 'D'}]}, # Nodo hoja
        {'valor': 'C', 'hijos': [{'valor': 'E'}, {'valor': 'F'}]} # Nodo hoja
    ]
}

# Llamamos a la función contar_nodos_hoja pasando el árbol como argumento y almacenamos el resultado
cantidad_nodos_hoja = contar_nodos_hoja(arbol)
# Imprimimos la cantidad de nodos hoja que tiene el árbol
print(f"El árbol tiene {cantidad_nodos_hoja} nodos hoja.")