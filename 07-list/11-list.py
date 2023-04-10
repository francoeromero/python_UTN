# Crea una lista de palabras y pide al usuario que ingrese una palabra. Luego, muestra todas las palabras de la lista que tienen la misma longitud que la palabra ingresada.
lista_palabras = ["medicina", "arquitectura", "abogacia", "ingenieria"]
n = input("Ingrese palabra: ")
for palabra in lista_palabras:
    if(palabra == n):
        esta_en_la_lista = True
        break
    else:
        esta_en_la_lista = False

if(esta_en_la_lista == True):
    print("Esta en la lista")
else:
    print("No esta en la lista")

