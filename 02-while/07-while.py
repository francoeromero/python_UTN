# Dada una lista de números, imprimir todos los números que son mayores que el promedio de la lista.

numeros = [1, 4, 3, 2, 12, 3, 5, 5]
suma = sum(numeros)
promedio = suma / len(numeros)
i = 0
while(i < len(numeros)):
    if (numeros[i] > promedio):
        print(numeros[i])
    i += 1
