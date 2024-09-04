'''
Realizar una funcion que permita sumar dos numero de las cuatro maneras siguientes
1 Una función sumar1 que reciba dos números y retorne el resultado
2 Una función sumar2 que reciba dos números y no retorne nada (o sea que la función se encargue de mostrar el resultado)
3 Una función sumar3 que no reciba nada y se encargue de pedir dos números y retornar el resultado
4 Una función sumar4 que no reciba nada y no retorne nada, por ende se va encargar de pedir los numeros y de mostrar el resultado.

'''


def sumar1(a:int,b:int)->int:
    r = a + b
    return r

def sumar2(a:int,b:int):
    r = a + b
    print(r)

def sumar3():
    a = int(input('ingrese numero: '))
    b = int(input('ingrese otro numero: '))
    r = a + b
    return r
def sumar4():
    a = int(input('ingrese numero: '))
    b = int(input('ingrese otro numero: '))
    r = a + b
    print(r)