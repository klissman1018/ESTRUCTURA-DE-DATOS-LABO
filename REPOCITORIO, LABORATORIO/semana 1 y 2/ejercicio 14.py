"14. Pide el radio de un círculo al usuario y calcula su área."

import math  # Importa el módulo math para acceder a funciones y constantes matemáticas

radio = float(input("Introduce el radio del círculo: "))  # Solicita al usuario el radio del círculo y lo convierte a flotante

area = math.pi * radio**2  # Calcula el área del círculo usando la constante pi del módulo math y elevando el radio al cuadrado

print("El área del círculo es:", area)  # Imprime el área calculada del círculo
  
radio = float(input("Ingrese el radio del círculo: "))  # Solicita nuevamente al usuario el radio del círculo y lo convierte a flotante
pi = 3.14159  # Define una aproximación de la constante pi
area = pi * radio ** 2  # Calcula el área del círculo usando la aproximación de pi y elevando el radio al cuadrado

print("El área del círculo es:", area)  # Imprime el área calculada del círculo