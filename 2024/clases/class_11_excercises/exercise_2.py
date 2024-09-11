'''
2. Crea una funcion que reciba una cadena y caracter. La funcion debera devolver el indice en el que se encuentre la primera incidencia de dicho caracter, o -1 en el caso de que no este 
'''

def first_occurrence(string:str,character:str):
    r = -1
    for i in range(len(string)):
        if character == string[i]:
            r = i
            break
    return r

print(first_occurrence("asdasdsa","a"))