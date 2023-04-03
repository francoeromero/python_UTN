# Dado un número entero n, imprimir la suma de todos los números impares menores o iguales a n.

# n_ingresado = input("Ingrese un numero: ")
# n = int(n_ingresado)
# suma = 0
# i = 0
# while(i < n):
#     if(i % 2 != 0):
#         suma = suma + i
#     i += 1
# print("La suma de todos los impares es ", suma)


n_ingresado = input("Ingrese un numero: ")
n = int(n_ingresado)
suma = 0
lista_numeros = ""
i = 0
while(i < n):
    if(i % 2 != 0):
        suma = suma + i
        lista_numeros = lista_numeros + ", " + str(i)
    i += 1
print("La lista de numeros es {0} y la suma de todos es {1}".format(lista_numeros, suma))
