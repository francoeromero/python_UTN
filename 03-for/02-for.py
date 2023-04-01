# Dada una lista de palabras, imprimir la palabra más larga de la lista.

# nombres = ["franco", "fernando", "katherine", "jorge"]
# print(len(nombres[0]))


# nombres = ["franco", "fernando", "katherine", "jorge"]
# nombre_mas_largo = len(nombres[0])
# print(nombre_mas_largo) # 6

nombres = ["franco", "fernando", "katherine", "jorge"]
nombre_mas_largo = nombres[2]
nombre_mas_corto = nombres[0]
for i in nombres:
    if(len(i) > len(nombre_mas_largo)):
        nombre_mas_largo = i
    if(len(i) < len(nombre_mas_corto)):
        nombre_mas_corto = i
print("El nombre mas largo es : {0} y el nombre mas corto es: {1} ".format(nombre_mas_largo, nombre_mas_corto))
