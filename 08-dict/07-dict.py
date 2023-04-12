# Crea un diccionario que contenga la información de una canción: título, artista y duración. Luego, imprime la duración de la canción.

canciones = [    
    {"titulo": "St Anger", 
    "artista": "Metallica", 
    "duracion": "2:30"},
        
    {"titulo": "el lugar es en donde parti",
    "artista": "La Renga",
    "duracion": "3:20"},

    {"titulo": "Thoughtless",
    "artista": "Korn",
    "duracion": "4:42"}]

for cancion in canciones:
    print(cancion["duracion"])