# Crea un diccionario que represente los juegos de una consola, donde las claves son los nombres de los juegos y los valores son las puntuaciones correspondientes. Solicita al usuario el nombre de un juego y luego su puntuación, si el juego no existe agregarlo y si existe actualizar su puntuación 

juegos = {
    "juego 1" : 4,
    "juego 2" : 2,
    "juego 3" : 19,
    "juego 4" : 1,
}
nombre = input("Ingrese un juego: ")
puntuacion = input("Ingrese una puntuacion : ")
puntuacion = int(puntuacion)
for i in juegos:
    if(i == nombre):
        juegos[i] = puntuacion
        break
print(juegos)