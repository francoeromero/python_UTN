# Crea una lista con 3 numeros enteros y luego agrega un nuevo numero al final de la lista
numeros = []
for numero in range(3):
    n = input("Ingrese un numero: ")
    n = int(n)
    numeros.append(n)
print("Lista antigua: ",numeros)
nuevo = input("Ingrese un numero nuevo: ")
nuevo = int(nuevo)
numeros.append(nuevo)
print("Lista nueva: ",numeros)
