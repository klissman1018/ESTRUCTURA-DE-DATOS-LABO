#7.     Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo). 

# Definimos una función para contar los nodos internos de un árbol
def contar_nodos_internos(nodo):
    # Si el nodo actual es None, significa que hemos llegado a un nodo hoja, por lo tanto, retornamos 0
    if nodo is None:
        return 0
    # Si el nodo tiene hijos, sumamos 1 (por el nodo actual) más la suma de los nodos internos de cada hijo
    elif nodo.get('hijos', []): 
        return 1 + sum(contar_nodos_internos(hijo) for hijo in nodo['hijos'])
    # Si el nodo no tiene hijos, es un nodo hoja, por lo tanto, no sumamos nada y retornamos 0
    else:
        return 0

# Creamos un diccionario que representa nuestro árbol, con un nodo raíz y sus respectivos hijos
arbol = {
    'valor': 'A', # Nodo raíz
    'hijos': [
        {'valor': 'B', 'hijos': [{'valor': 'D'}]}, # Nodo interno B con un hijo D
        {'valor': 'C', 'hijos': [{'valor': 'E'}, {'valor': 'F'}]} # Nodo interno C con dos hijos E y F
    ]
}

# Llamamos a la función contar_nodos_internos pasando el árbol como argumento para obtener la cantidad de nodos internos
cantidad_nodos_internos = contar_nodos_internos(arbol)
# Imprimimos la cantidad de nodos internos en el árbol
print(f"El árbol tiene {cantidad_nodos_internos} nodos internos.")