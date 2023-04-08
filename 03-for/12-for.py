# Dada una lista de números, imprimir la cantidad de números pares en la lista.
lista = []

for i in range(5):
    n_ingresado = input("Ingrese un numero: ")
    n = int(n_ingresado)
    if(n % 2 == 0):
        lista.append(n)
print(lista)
