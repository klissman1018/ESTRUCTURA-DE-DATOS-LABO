#Búsqueda de rutas en un laberinto
#3.    Desarrolla un programa que encuentre el camino más corto a través de un laberinto. Utiliza una cola 
#para realizar un recorrido en anchura (BFS) desde el punto de inicio hasta el punto de destino.

from collections import deque  # Importa deque de collections para usar colas

def encontrar_camino(laberinto):  # Define una función para encontrar el camino en un laberinto
    # Encontrar la posición inicial y final
    for i in range(len(laberinto)):  # Itera sobre las filas del laberinto
        for j in range(len(laberinto[0])):  # Itera sobre las columnas del laberinto
            if laberinto[i][j] == 'S':  # Si encuentra el inicio 'S'
                inicio = (i, j)  # Guarda la posición de inicio
            if laberinto[i][j] == 'D':  # Si encuentra el destino 'D'
                destino = (i, j)  # Guarda la posición de destino

    # Inicializar la cola y el diccionario de visitados
    cola = deque([inicio])  # Inicializa la cola con la posición de inicio
    visitados = {inicio: None}  # Inicializa el diccionario de visitados con la posición de inicio

    while cola:  # Mientras haya elementos en la cola
        x, y = cola.popleft()  # Extrae el primer elemento de la cola
        if (x, y) == destino:  # Si la posición actual es el destino
            # Construir el camino más corto
            camino = []  # Inicializa la lista del camino
            while (x, y) != inicio:  # Mientras no se llegue al inicio
                camino.append((x, y))  # Añade la posición actual al camino
                x, y = visitados[(x, y)]  # Retrocede al punto anterior
            camino.append(inicio)  # Añade la posición de inicio al camino
            camino.reverse()  # Invierte el orden del camino para que vaya de inicio a destino
            return camino  # Retorna el camino encontrado

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Itera sobre las 4 direcciones posibles
            nx, ny = x + dx, y + dy  # Calcula la nueva posición
            if (0 <= nx < len(laberinto)) and (0 <= ny < len(laberinto[0])) and (laberinto[nx][ny] != '#') and (nx, ny) not in visitados:  # Si la nueva posición es válida y no ha sido visitada
                cola.append((nx, ny))  # Añade la nueva posición a la cola
                visitados[(nx, ny)] = (x, y)  # Marca la nueva posición como visitada y guarda de dónde se vino

    return None # No se encontró un camino. Retorna None si no se encuentra un camino

# Ejemplo de laberinto
laberinto = [
    ['S', '.', '.', '.', '.', '#', '#', '#', '#'],
    ['#', '.', '#', '#', '#', '.', '#', '#', '#'],
    ['#', '.', '.', '.', '#', '.', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '.', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', 'D'],
]

camino = encontrar_camino(laberinto)  # Llama a la función para encontrar el camino en el laberinto
if camino:  # Si se encontró un camino
    print("Camino encontrado:")  # Imprime un mensaje
    for x, y in camino:  # Itera sobre las posiciones del camino
        print(f"({x}, {y})", end=" -> ")  # Imprime cada posición del camino
    print("Destino")  # Imprime el destino al final
else:  # Si no se encontró un camino
    print("No se encontró un camino.")  # Imprime un mensaje indicando que no se encontró un camino