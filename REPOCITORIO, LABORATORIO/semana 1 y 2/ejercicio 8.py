"8. Crea una lista de los cuadrados de los primeros 10 números naturales."

# Se crea una lista llamada lista_cuadrados. Esta lista se llena con los cuadrados de los primeros 10 números naturales.
# Se utiliza una comprensión de lista para generar los cuadrados de los números del 1 al 10.
lista_cuadrados = [numero ** 2 for numero in range(1, 11)]

# Se imprime un mensaje para indicar que a continuación se mostrará la lista de cuadrados.
print("Lista de los cuadrados de los primeros 10 números naturales:")
# Se imprime la lista lista_cuadrados, que contiene los cuadrados de los primeros 10 números naturales.
print(lista_cuadrados)