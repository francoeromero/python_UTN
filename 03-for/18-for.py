# Dada una lista de números, imprimir la suma de los números en la lista que son mayores que el promedio de la lista.

numeros = [1, 2, 3, 4, 5]
suma = 0
suma_mayores_promedio = 0
numeros_mayores_promedio = []
promedio = sum(numeros) / len(numeros)

for i in numeros:
    if(i > promedio):
        suma_mayores_promedio += i
        numeros_mayores_promedio.append(i)
print("Los numeros mayores que el promedio son: {} y la suma de todos es de: {}".format(numeros_mayores_promedio, suma_mayores_promedio))
