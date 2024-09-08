'''
3. crea una funcion que reciba como parametro una cadena y determina si es palindromo debera retornar un valor booleano 
'''

def is_palindromo(string:str)->bool:
    j = 0
    r = False
    for i in range(len(string)-1,-1,-1):
        if string[i] == string[j]:
            r = True
        j += 1
    return r

print(is_palindromo('ala'))
