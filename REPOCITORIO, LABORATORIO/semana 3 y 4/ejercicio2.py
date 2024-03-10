"Ejercicio 2: Escribe una función recursiva que imprima la suma de los números del 1 al n."

def suma_recursiva(n):
    # Esta función calcula la suma de todos los números desde 1 hasta n de manera recursiva.
    
    if n == 0:
        # Si n es igual a 0, la función retorna 0. Este es el caso base de la recursión.
        return 0
   
    else:
        # Si n no es 0, la función se llama a sí misma con n-1 y suma n al resultado.
        # Esto continúa hasta que n sea 0, sumando todos los números desde 1 hasta n.
        return n + suma_recursiva(n - 1)

n = int(input("Ingrese un número: "))
# Esta línea pide al usuario que ingrese un número y lo convierte a entero. Este número se asigna a la variable n.

print("La suma de los números del 1 al", n, "es : ", suma_recursiva(n))
# Esta línea imprime el resultado de la función suma_recursiva con el número ingresado por el usuario.
# Muestra la suma de todos los números desde 1 hasta n.
