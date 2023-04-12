# Dado un número entero n, imprimir la secuencia de números triangulares menores o iguales a n.

n = input("Ingrese un numero: ")
n = int(n)

triangulares = []
suma = 0

for i in range(1, n+1):
    suma += i 
    if(suma > n):
        break
    triangulares.append(suma)

for numero in triangulares:
    print(numero)
print("La secuencia de ")