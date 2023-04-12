# Crea un diccionario que contenga el nombre y el nivel de dificultad de varios juegos de mesa. Luego, pedirle al usuario un nivel de dificultad, buscar los que coinciden e imprimir sus nombres

juegos = {
    "lol" : "dificil",
    "counter strike" : "facil",
    "valorant" : "medio",
    "tetris" : "facil",
    "dota" : "medio",
    "gta" : "dificil"
}
juegos_recomendados = []
n = input("Ingrese nivel de dificultad, facil, medio o dificil: ")
for i in juegos:
    if(juegos[i] == n):
        juegos_recomendados.append(i)
print("Los juegos que te recomiendo son: ", juegos_recomendados)

