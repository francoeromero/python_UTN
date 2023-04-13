# Crea un diccionario que represente los juegos de una consola, donde las claves son los nombres de los juegos y los valores son las puntuaciones correspondientes. Solicita al usuario el nombre de un juego y luego su puntuación, si el juego no existe agregarlo y si existe actualizar su puntuación 

#para agregar un elemento en un diccionario 
# diccionario = {}
# diccionario["clave"] = "valor"
# print(diccionario)
# #para agregar un elemento a una lista
# lista = []
# lista.append(1)
# print(lista)

juegos = {
    "juego 1" : 4,
    "juego 2" : 2,
    "juego 3" : 19,
    "juego 4" : 1,
}


nombre = input("Ingrese un juego: ")
puntuacion = input("Ingrese una puntuacion : ")
puntuacion = int(puntuacion)
juegos[nombre] = puntuacion

print(juegos)