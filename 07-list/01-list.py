# Crea una lista con los números del 1 al 10 e imprime solo los números impares.
lista = range(0, 11) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lista:
    if(i % 2 != 0):
        print(i)

# i = 0
# while(i < len(lista)):
#     if(i % 2 != 0):
#         print(lista[i])
#     i += 1