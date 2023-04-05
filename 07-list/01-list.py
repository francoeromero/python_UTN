# Crea una lista con los números del 1 al 10 e imprime solo los números impares.
lista = range(0, 11)
for i in lista:
    if(i % 2 != 0):
        print(i)