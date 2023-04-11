# Crea una lista con los nombres de tus 3 películas favoritas y luego imprime los elementos en orden inverso (sin utilizar el método reverse())

peliculas = ["Rey leon", "Matrix", "300"]
lista_orden_inverso = []
i = 2
while(i > -1):
    lista_orden_inverso.append(peliculas[i])
    i -= 1
print(lista_orden_inverso)

