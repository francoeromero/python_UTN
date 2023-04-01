# Dado un número entero n, imprimir la secuencia de números impares menores o iguales a n.

n_ingresado = input("Ingrese un numero: ")
n = int(n_ingresado)
lista_impares = list(range(0, 11))
for i in lista_impares:
    if(not(i % 2 == 0) and i <= n):
        print(i)
