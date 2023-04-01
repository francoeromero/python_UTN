# Dada una lista de palabras, imprimir las palabras que comienzan y terminan con la misma letra.




nombres = ["franco", "manuel", "fernando", "federico", "gabriel", "oso"]
for nombre in nombres:
    if nombre[0] == nombre[-1]:
        print(nombre)


palabras = ["amigo", "casa", "sol", "anaconda", "oso", "perro", "oto"]
i = 0
for palabra in palabras:
    if(palabra[0] == palabra[-1]):
        print(palabra)






# nombres = ["franco", "manuel", "fernando", "federico", "gabriel"]
# primera_letra = nombres[0][0]
# print(primera_letra) # del segundo corchetes imprime la primera letra de franco 

# nombres = ["franco", "manuel", "fernando", "federico", "gabriel"]
# primera_letra = nombres[0][-1]
# print(primera_letra) # del segundo corchetes imprime la ultima letra de franco 
