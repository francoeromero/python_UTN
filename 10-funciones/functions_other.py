'''
Ejercitación Clase 5 (Funciones Avanzado)


1. Desarrollar una función que verifique el DNI de una persona, la misma recibirá un str (se asume que solamente contiene caracteres numéricos). Si la cantidad de caracteres es menor a 6 o mayor a 8, retornara False. Si la cantidad de caracteres está comprendida entre 6 y 8 devolverá True

Para saber la cantidad de elementos de un str usamos la función len()

2. Desarrollar una función que complete el número de DNI de una persona. Recibirá un str (se asume que solamente contiene caracteres numéricos), deberá medirla (len) y completar con ceros a la izquierda hasta llegar a un total de 8 caracteres, y devolviendo la cadena resultante. 
En caso de que el dni sea invalido (que no tiene entre 6 y 8 caracteres) devolvera una cadena que dice : “DNI INVALIDO”

Ej: Se ingresa “12345”, y devolverá “DNI INVALIDO”.
Ej: Se ingresa “123456”, y devolverá “00123456”.
Ej: Se ingresa “1234567”, y devolverá “01234567”.
Ej: Se ingresa “12345678”, y devolverá “12345678”.
Ej: Se ingresa “123456789”, y devolverá “DNI INVALIDO”.

Nota: Reutilizar la función del ejercicio 1 para validar si el dni es válido


'''

def verify_dni(dni:str)->bool:
    if len(dni) < 6 or len(dni) > 8:
        return False
    else:
        return True
print(verify_dni('12345678'))

def complete_dni(document:str)->str:
    verification = verify_dni(document)
    
    if verification == True:
        end = 8 - len(document)
        for i in range(0,end,1):
            document = '0' + document
        return document
    else:
        return 'DNI INVALIDO'
    
print(complete_dni('12345'))
print(complete_dni('123456'))
print(complete_dni('1234567'))
print(complete_dni('12345678'))
print(complete_dni('123456789'))