"10. Genera los primeros 10 números de la serie Fibonacci."

def generar_fibonacci(n):
   # Inicializa la lista de Fibonacci con los dos primeros números, 0 y 1.
   fibonacci = [0, 1]
   # Itera desde 2 hasta n para generar los números de Fibonacci.
   for i in range(2, n):
       # Añade el nuevo número de Fibonacci a la lista, que es la suma de los dos anteriores.
       fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
       
   # Devuelve la lista completa de números de Fibonacci hasta n.
   return fibonacci
# Llama a la función generar_fibonacci con 10 como argumento y muestra el resultado.
print(generar_fibonacci(10))