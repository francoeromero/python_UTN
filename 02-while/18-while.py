# Dado un número entero n, imprimir la suma de todos los números que son múltiplos de 5 menores o iguales a n.

n_ingresado = input("Ingrese un numero: ")
n = int(n_ingresado)
i = 1
suma = 0
lista_multiplos = ""
while(i <= n):
    if(i % 5 == 0):
        suma += i
        lista_multiplos += str(i) + " "
    i += 1
print("La lista multiplos de 5 es: {0} y la suma de todos es: {1}".format(lista_multiplos, suma))


# n_ingresado = input("Ingresa un numero: ")
# n = int(n_ingresado)
# i = 5
# suma = 0
# lista = ""
# while(i <= n):
#     if(i % 5 == 0):
#         suma += i
#         lista += str(i) + " "
#     i += 5
# print("La lista de multiplos es: {0} y la suma de todos es: {1}".format(lista, suma))









