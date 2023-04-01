# Dado un número entero n, imprimir la suma de los números impares menores o iguales a n.

n_ingresado = input("Ingrese el numero: ")
n = int(n_ingresado)
numeros = list(range(0, 11))
for i in numeros:
    if(not(i % 2 == 0) and i <= n):
        print(i)
    