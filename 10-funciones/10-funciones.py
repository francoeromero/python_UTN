# Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.

palabras = [ "elefante", "colibri", "tigre", "camello"]

def palabra_mas_largo(lista_palabras):
    bandera = 0
    for i in palabras:
        if(len(i) > len(max_letras) | bandera == 0):
            max_letras = i 
            bandera = 1
    return max_letras
print(palabra_mas_largo(palabras))