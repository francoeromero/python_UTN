'''
crear una funcion que reciba como parametro una cadena y suprima los caracteres repetitivos. ej: hooooolaaa,  hola
'''

def summarize_string(string:str):
    acumulater = ''
    for i in range(len(string)):
       if i == 0:
           acumulater += string[i]
       elif string[i] != string[i-1]:
            acumulater += string[i]
    return acumulater

print(summarize_string('hhhhhoooooollllaaa'))

