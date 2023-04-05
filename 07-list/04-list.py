# Crea una lista vacía y pide al usuario que ingrese una palabra. Luego, muestra la primera letra de la palabra. Repite este proceso hasta que el usuario ingrese una palabra que comience con la letra "z".

lista = []
i = True
while(i):
    palabra = input("Ingrese una palabra: ")
    if(palabra[0] == "z"):
        break
    else:
        lista.append(palabra[0])
print("lista: {0}".format(lista))