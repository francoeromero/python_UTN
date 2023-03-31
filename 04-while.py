# Dada una lista de números, imprimir la suma de todos los elementos de la lista.

# lista = list(range(5))
# print(lista)

lista = [1, 2, 3]
# print(len(lista))
inicio = 0
acumulador = 0
while (inicio < len(lista)):
    acumulador += lista[inicio]
    inicio = inicio + 1
print("la suma de los numeros de la lista", acumulador)


# lista = [1, 2, 3, 4, 5]
# inicio = 0
# while (lista[0] <):
