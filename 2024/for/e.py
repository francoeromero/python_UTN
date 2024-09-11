'''
10 crear una funcion con parametros que dada una palabra, cuenta la cantidad total de letras y retorne dicha cantidad como un entero
'''

def count_word(word:int):
    number = 0
    for i in word:
        number += 1
    return number
print(count_word('hola'))

'''
crear una funcion sin parametros que pida al usuario que ingrese tres palabras, y calculara cual de ellas tiene mayor cantidad de caracteres  y tendra que imprimirla en consola junto con la cantidad
'''

def show_larger_number_characters(string_1:str, string_2:str, string_3:str):
    strings = [string_1,string_2,string_3]
    larger_number_characters = len(strings[0])
    string_larger = strings[0]
    for i in range(len(strings)):
        if len(strings[i]) > larger_number_characters:
            larger_number_characters = len(strings[i])
            string_larger = strings[i]
    return f'\n{string_larger}\nnumber of characters: {larger_number_characters}'

print(show_larger_number_characters('aa','bvb','sdadsada'))

