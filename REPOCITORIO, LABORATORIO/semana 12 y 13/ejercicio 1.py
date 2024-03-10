#Ejercicio parte 01 –  Colas:
#Verificar si una palabra es palíndroma
#1. Implementa una función que determine si una palabra es palíndroma o no. Utiliza una cola para comparar los caracteres de la palabra en orden original y reverso.

from collections import deque  # Importa la clase deque de la biblioteca collections para usar colas

def es_palindromo(palabra):  # Define una función para verificar si una palabra es un palíndromo

    palabra = palabra.lower()  # Convierte la palabra a minúsculas para hacer la comparación insensible a mayúsculas
    
    cola = deque()  # Crea una cola vacía para almacenar los caracteres de la palabra
    for char in palabra:  # Itera sobre cada carácter de la palabra
        if char.isalpha():  # Verifica si el carácter es una letra
            cola.append(char)  # Si es una letra, la añade al final de la cola
    
    while len(cola) > 1:  # Mientras haya más de un carácter en la cola
        primer_caracter = cola.popleft()  # Elimina y devuelve el primer carácter de la cola
        ultimo_caracter = cola.pop()  # Elimina y devuelve el último carácter de la cola
        
        if primer_caracter != ultimo_caracter:  # Compara los dos caracteres
            return False  # Si son diferentes, la palabra no es un palíndromo y retorna Falso
    
    return True  # Si todos los caracteres coinciden, la palabra es un palíndromo y retorna Verdadero

palabra = "Anita lava la tina"  # Define una palabra para verificar
if es_palindromo(palabra):  # Llama a la función es_palindromo y verifica si la palabra es un palíndromo
    print("La palabra es un palíndromo.")  # Si es un palíndromo, imprime este mensaje
else:
    print("La palabra no es un palíndromo.")  # Si no es un palíndromo, imprime este mensaje