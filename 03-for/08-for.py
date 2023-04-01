# Dado un número entero n, imprimir la suma de los números pares menores o iguales a n.

n_ingresado = input("Ingrese un numero: ")
n = int(n_ingresado)
acumulador_pares = 0
lista_pares = list(range(0, 20))
for i in lista_pares:
    if(i % 2 == 0):
        acumulador_pares += i
print("La suma de los pares es : ", acumulador_pares)
