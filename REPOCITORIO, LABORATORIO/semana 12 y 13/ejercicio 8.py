#Calcular altura y profundidad:
#8.    Implementar una función que calcule la altura del árbol (la longitud del camino más largo desde la raíz 
#hasta una hoja).

class Nodo:
    # Esta función inicializa un nuevo nodo con un valor dado.
    # 'self.valor' almacena el valor del nodo.
    # 'self.izquierdo' y 'self.derecho' son punteros a los nodos hijos izquierdo y derecho, respectivamente, inicializados en None.
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Esta función calcula la altura de un árbol binario.
def altura_arbol(nodo):
    # Si el nodo actual es None, significa que hemos alcanzado una hoja o el árbol está vacío, por lo que retornamos 0.
    if nodo is None:
        return 0
    else:
        # Calculamos la altura del subárbol izquierdo recursivamente.
        altura_izquierda = altura_arbol(nodo.izquierdo)
        # Calculamos la altura del subárbol derecho recursivamente.
        altura_derecha = altura_arbol(nodo.derecho)
        # Retornamos el mayor de los dos valores obtenidos (altura izquierda o derecha) más uno, que representa el nodo actual.
        return max(altura_izquierda, altura_derecha) + 1

# Creamos el nodo raíz del árbol con valor 1.
nodo_raiz = Nodo(1)
# Asignamos un nodo con valor 2 como hijo izquierdo del nodo raíz.
nodo_raiz.izquierdo = Nodo(2)
# Asignamos un nodo con valor 3 como hijo derecho del nodo raíz.
nodo_raiz.derecho = Nodo(3)
# Asignamos un nodo con valor 4 como hijo izquierdo del hijo izquierdo del nodo raíz.
nodo_raiz.izquierdo.izquierdo = Nodo(4)
# Asignamos un nodo con valor 5 como hijo derecho del hijo izquierdo del nodo raíz.
nodo_raiz.izquierdo.derecho = Nodo(5)

# Calculamos la altura del árbol comenzando desde el nodo raíz.
altura = altura_arbol(nodo_raiz)
# Imprimimos la altura del árbol.
print(f"La altura del árbol es {altura}.")