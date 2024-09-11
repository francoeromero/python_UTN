'''
1. Crea una funcion que reciba como parametro una cadena y determine la cantidad de vocales que hay en cada una individualmente.
la funcion retornara una matriz indicando en la columna 1 cada vocal y en la columna 2 la cantidad.
ejemplo: 
cadena = "murcielago"
'a' 1
'e' 1
'i' 2
'o' 1
'u' 2
'''
def counter_vowels(string:str):
    vowels = ['a','e','i','o','u']
    matrix = []
    for i in range(len(vowels)):
        counter = 0
        subarray = [vowels[i]]
        for j in range(len(string)):
            if string[j] == vowels[i]:
                counter += 1
        subarray.append(counter)
        matrix.append(subarray)
    return matrix
print(counter_vowels('gorila'))

