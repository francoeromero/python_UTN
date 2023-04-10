# Dada una lista de palabras, imprimir las palabras que tienen una letra específica.

lista_palabras = ["hola mundo", "que tal", "como estas", "todo bien"]

# el i representa cada palabra
# el a repressenta cada letra de la palabra
for i in range(len(lista_palabras)): # daria 4 vueltas porque son 4 paalbras
    for a in range(len(lista_palabras[i])): # de cada palabra dara vueltas segun cant de letras
            if(lista_palabras[i][a] == "q"): # si en una de esas letras es q 
                print(lista_palabras[i]) # se imprime la palabra con q




