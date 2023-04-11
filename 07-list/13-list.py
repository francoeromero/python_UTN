# Crea una lista de números y encuentra el promedio de todos los números en la lista.

numeros = [1, 3, 2]
suma = 0
for i in numeros:
    suma += i
promedio = suma / len(numeros)
print("La suma es {} y el promedio es {}".format(suma, promedio))