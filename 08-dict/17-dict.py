# Crea un diccionario que represente las películas de un cine, donde las claves son los nombres de las películas y los valores son los horarios correspondientes. Modifica el horario de la película "Avengers: Endgame" a las 19:30.

peliculas = {
    "forest gump" : "18:30",
    "luna" : "19:10",
    "titanic" : "22:00",
    "avengers endgame " : "17:30"
}
n = input("Ingrese la pelicula que quiere cambiar el horario: ")
cambio_horario = input("Ingrese el horario nuevo: ")
for i in peliculas:
    if(i == n):
        peliculas[i] = cambio_horario
print(peliculas)