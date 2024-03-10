"Ejercicio 3: Escribe una función recursiva que imprima la pirámide de números del 1 al n."


def imprimir_piramide(n, current=1):
    # Define una función llamada imprimir_piramide que toma dos argumentos: n (el número total de niveles de la pirámide) y current (el nivel actual de la pirámide que se está imprimiendo, con un valor predeterminado de 1)
    
    # Si el nivel actual es mayor que el número total de niveles, termina la función
    if current > n:  
        return
    
    # Imprime espacios en blanco para alinear los números a la derecha y luego los números del 1 al nivel actual, separados por espacios
    print(" " * (n - current) + " ".join(str(i) for i in range(1, current + 1)))
    
    # Llama a la misma función incrementando el nivel actual para construir el siguiente nivel de la pirámide
    imprimir_piramide(n, current + 1)

# Solicita al usuario ingresar el número total de niveles para la pirámide y lo convierte a entero
n = int(input("Ingrese el número de niveles de la pirámide: "))
# Llama a la función para imprimir la pirámide con el número de niveles especificado
imprimir_piramide(n)
