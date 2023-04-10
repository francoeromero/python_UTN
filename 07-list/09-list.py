# Crea una lista de números enteros y pide al usuario que ingrese otro número entero. Luego, busca el número ingresado en la lista y muestra la posición en la que se encuentra. Si el número no se encuentra en la lista, muestra un mensaje indicando que no se encontró

# lista_palabras = ["casa","perro","medicina","veterinaria","gato"]

# palabra = input("ingrese palabra: ")
# bandera = False

# for palabras in lista_palabras:
#     if palabras == palabra:
#         for indice in range(len(lista_palabras)):
#             if lista_palabras[indice] == palabra:
#                 bandera=True
#                 break

# if bandera==True:
#     print("La palabra {} esta en la lista y esta en el indice {}".format(palabra,indice+1))
# else:
#     print("La palabra no esta en la lista")






lista_palabras = ["medicina", "esdicina", "arquitectura", "abogacia", "ingenieria"]
n = input("Ingrese palabra: ")
lista_misma_longitud = []
bandera = False
for palabra in lista_palabras:
    if palabra == n:
        for indice in range(len(lista_palabras)):
            if lista_palabras[indice] == n:
                bandera = True
                break

for i in lista_palabras:
    if(len(n) == len(i)):
        lista_misma_longitud.append(i)
print(lista_misma_longitud)

if bandera == True:
    print("La palabra {0} esta en la lista y esta en el indice {1}".format(n, indice+1))
else:
    print("La palabra no esta en la lista")






# for palabra in lista_palabras:
#     if(palabra == n):
#         print("Esta en la lista")
#         break

# if(palabra != n):
#     print("No esta en la lista")

# for palabra in lista_palabras:
#     if(palabra == n):
#         esta_en_la_lista = True
#         break
#     else:
#         esta_en_la_lista = False

# if(esta_en_la_lista == True):
#     print("Esta en la lista")
# else:
#     print("No esta en la lista")



# numero = input("Ingrese un numero: ")
# numero = int(numero)
# numeros = [1, 3, 2, 5, 8, 0, 2, 6]
# i = 0
# while(i < len(numeros)):
#     numero_ingresado = input("Ingrese un numero : ")
#     numero = int(numero_ingresado)
#     if(i == numero):
#         print("el numero es {} y esta en la lista su posicion es: {}".format(i, numeros.index(i)))
#         break
#     i += 1

# for i in numeros:
#     numero_ingresado = input("Ingrese un numero : ")
#     numero = int(numero_ingresado)
#     if(i == numero):
#         print("El numero {} esta en la lista su posicion es: {}".format(i, numeros.index(i)))

