# Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.

palabras = [ "elefante", "colibri", "tigre", "camello"]

def palabra_mas_larga(lista_palabras):
    palabra_mas_larga = ''
    for palabra in lista_palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga