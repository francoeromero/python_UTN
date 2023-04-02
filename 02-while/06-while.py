# Dado un número entero n, imprimir la suma de todos los números pares menores o iguales a n
# 1 : detectar numeros pares
# 2 : acumular esos pares
n_ingresado = input("Ingrese un numero: ")
n = int(n_ingresado)
numeros = list(range(0, 11))
i = 0
a = 0
while(i < n):
    print(numeros[i] % 2 == 0 and n == i):
        a += numeros[i]
        i = i + 1