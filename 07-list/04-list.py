# Crea una lista vacía y pide al usuario que ingrese una palabra. Luego, muestra la primera letra de la palabra. Repite este proceso hasta que el usuario ingrese una palabra que comience con la letra "z".

# lista = []
# i = True
# while(i):
#     palabra = input("Ingrese una palabra: ")
#     if(palabra[0] == "z"):
#         break
#     else:
#         lista.append(palabra[0])
# print("lista: {0}".format(lista))

palabras = []
palabra = input("Ingrese una palabra: ")
for i in range(len(palabra)):
    if(palabra[i] == "z"):
        break
    else:
        palabras.append(palabra)
print("la lista es: ", palabras)
# for i in range(0, 11):
#     print(i)