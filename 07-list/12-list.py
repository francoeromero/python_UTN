# Crea una lista con los nombres de tus 3 películas favoritas y luego imprime los elementos en orden inverso (sin utilizar el método reverse())

peliculas = ["Rey leon", "Matrix", "300"]
lista_orden_inverso = []
# con while
# i = 2
# while(i > -1):
#     lista_orden_inverso.append(peliculas[i])
#     i -= 1
# print(lista_orden_inverso)
# con for 
for i in range(2, -1, -1):
    lista_orden_inverso.append(peliculas[i])
print(lista_orden_inverso)


#TEORIA
#reversed hace que imprimas de 2 a 0 
# for i in reversed(range(3)):
#     print(i)

# si no queres usar reversed, usas range(inicio, final, direccion)
# for i in range(2, -1, -1):
#     print(i)