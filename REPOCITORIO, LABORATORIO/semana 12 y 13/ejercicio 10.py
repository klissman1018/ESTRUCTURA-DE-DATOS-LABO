#Buscar el mínimo y el máximo:
#10.  Implementar una función que encuentre el nodo con el valor mínimo en el árbol.

class Nodo:
    # Esta función inicializa un nuevo nodo con un valor dado.
    # También establece los nodos hijo izquierdo y derecho como None por defecto.
    def __init__(self, valor):
        self.valor = valor  # Almacena el valor del nodo.
        self.izquierdo = None  # Inicializa el nodo hijo izquierdo como None.
        self.derecho = None  # Inicializa el nodo hijo derecho como None.

# Esta función busca el nodo con el valor mínimo en el árbol.
def nodo_minimo(nodo):
    # Si el nodo actual es None, significa que hemos llegado al final del árbol sin encontrar un nodo.
    if nodo is None:
        return None
    # Si el nodo actual no tiene hijo izquierdo, significa que este nodo es el mínimo.
    elif nodo.izquierdo is None:
        return nodo
    # Si el nodo actual tiene un hijo izquierdo, buscamos recursivamente el nodo mínimo en el subárbol izquierdo.
    else:
        return nodo_minimo(nodo.izquierdo)

# Ejemplo de uso
nodo_raiz = Nodo(50)  # Crea el nodo raíz con valor 50.
nodo_raiz.izquierdo = Nodo(30)  # Asigna un nodo hijo izquierdo con valor 30 al nodo raíz.
nodo_raiz.derecho = Nodo(70)  # Asigna un nodo hijo derecho con valor 70 al nodo raíz.
nodo_raiz.izquierdo.izquierdo = Nodo(20)  # Asigna un nodo nieto izquierdo con valor 20.
nodo_raiz.izquierdo.derecho = Nodo(40)  # Asigna un nodo nieto derecho con valor 40.
nodo_raiz.derecho.izquierdo = Nodo(60)  # Asigna otro nodo nieto izquierdo con valor 60.
nodo_raiz.derecho.derecho = Nodo(80)  # Asigna otro nodo nieto derecho con valor 80.

nodo_min = nodo_minimo(nodo_raiz)  # Busca el nodo con el valor mínimo en el árbol.
if nodo_min:
    print(f"El nodo con el valor mínimo es {nodo_min.valor}.")  # Imprime el valor del nodo mínimo.
else:
    print("El árbol está vacío.")  # Imprime un mensaje si el árbol está vacío.
