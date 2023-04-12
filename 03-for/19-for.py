# Dada una lista de palabras, imprimir las palabras que tienen una letra mayúscula.

palabras = ["HOLA", "holas", "Hola", "HELLO"]
# for i in palabras:
#     if(i.isupper()):
#         print(i)

#creo una lista vacia
letras_mayusculas = []
#hago un for que pase por todas las palabras
for palabra in palabras:
    #luego hago que en cada palabra pase por cada letra
    for letra in palabra:
        # si la letra tiene mayuscula se imprime y se agrega ala lista
        if(letra.isupper()):
            print(letra)
            letras_mayusculas.append(letra)
# imprimo la lista de letras mayusculas
print(letras_mayusculas)

