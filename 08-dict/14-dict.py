# Crea un diccionario que contenga el nombre como clave y el puntaje como valor de varios jugadores en un juego. Luego, pedirle al usuario el nombre del jugador y nuevo puntaje y actualizar el valor correspondiente en el diccionario.

jugadores = {
    "juancito" : 23,
    "jose" : 32,
    "julian" : 20
}
nombre = input("Ingrese el nombre del jugador: ")

if nombre in jugadores:
    puntaje = input("Ingrese el nuevo puntaje de {} : ".format(nombre))
    puntaje = int(puntaje)
    jugadores[nombre] = puntaje
    print(jugadores)
else:
    print("Nombre del jugador no valido")