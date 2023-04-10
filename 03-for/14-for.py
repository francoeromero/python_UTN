# Dada una lista de números, imprimir la cantidad de números impares en la lista.
lista_numeros = []

for i in range(5):
    n = input("Ingrese un numero: ")
    n = int(n)
    if(n % 2 != 0):
        lista_numeros.append(n)
print(lista_numeros)