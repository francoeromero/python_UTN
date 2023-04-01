# Dada una lista de números, imprimir el número más grande de la lista.

numeros = [2, 4, 6, 8, 10]
maximo = numeros[3]
minimo = numeros[1]
for i in numeros:
    if(i > maximo):
        maximo = i
    if(i < minimo):
        minimo = i
print("El maximo", maximo, "El minimo", minimo)


# numeros = [1, 2, 3, 4, 5]
# num = True
# for i in numeros:
#     if(num == True):
#         print(i)
#         num = False


# numeros = [3, 4, 1, 9]
# for i in numeros:
#     print(i) # imprime cada numero de la lista

# nombres = ["Fran", "Juan", "Fernando", "Katherine"]
# for i in nombres:
#     print(i) # imprime cada nombre de la lista

## suma de pares 

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# acumulador_pares = 0
# for i in numeros:
#     if (i % 2 == 0):
#         acumulador_pares = acumulador_pares + i
# print("La suma de los numeros pares es: ", acumulador_pares)

# numeritos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# acumulador_impares = 0
# for i in numeritos:
#     if(not(i % 2 == 0)):
#         acumulador_impares = acumulador_impares + i
# print("La suma de los impares es", acumulador_impares)

# def tabla_multiplicar(numero):
#     for i in range(1, 11):
#         print(numero, "x", i, "=", (numero * i))
# tabla_multiplicar(6)












# def lista_mas_grande():
#     # creo una variable y asigno una lista de numeros
#     lista = [0, 2, 4, 6, 8, 10, 12, 20]
#     # creo otra variable y le asigno el primer elemento de la lista
#     maximo = lista[0]
#     # for
#     for numero in lista:
#         if numero > maximo:
#             maximo = numero
#     print("El numero más grande en la lista es: ", maximo)
# lista_mas_grande()

# def lista_mas_chica():
#     lista = [23, 5, 62, 3, 7]
#     minimo = lista[0]
#     for numero in lista:
#         if numero < minimo:
#             minimo = numero
#     print("El numero más chico es ", minimo)
# lista_mas_chica()