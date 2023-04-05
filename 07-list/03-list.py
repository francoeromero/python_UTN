# Crea una lista vacía y pide al usuario que ingrese números enteros hasta que ingrese un número negativo. Luego, muestra la suma de todos los números ingresados.

lista = []

for i in range(5):
    numero_ingresado = input("Ingrese un numero: ")
    numero = int(numero_ingresado)
    lista.append(numero)
print(lista)




# suma = 0
# i = True
# while(i):
#     n_ingresado = input("Ingrese un numero: ")
#     n = int(n_ingresado)
#     if(n < 0):
#         print(n)
#         break
#     lista.append(n)
#     suma += n
# print("la lista es: {0} y la suma de todos es : {1}".format(lista, suma))