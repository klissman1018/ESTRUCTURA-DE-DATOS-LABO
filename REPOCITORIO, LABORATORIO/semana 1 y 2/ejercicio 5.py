"5. Verifica si un número ingresado por el usuario es primo o no."

def es_primo(n):  # Define una función para determinar si un número es primo
   if n < 2:  # Si el número es menor que 2, automáticamente no es primo
       return False  # Retorna Falso porque no es primo
   for i in range(2, int(n**0.5) + 1):  # Itera desde 2 hasta la raíz cuadrada de n para verificar divisores
       if n % i == 0:  # Si n es divisible por i, entonces n no es primo
           return False  # Retorna Falso porque encontró un divisor, por lo tanto, no es primo
   return True  # Si no se encontraron divisores, retorna Verdadero indicando que es primo

numero = int(input("Ingrese un número: "))  # Solicita al usuario ingresar un número y lo convierte a entero
# Utiliza la función es_primo para verificar si el número ingresado es primo y lo imprime
print(f"{numero} es {'primo' if es_primo(numero) else 'no primo'}")
