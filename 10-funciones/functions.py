def calcular_promedio(acumulador:int,contador:int):
    '''
    1.Crear una función que reciba dos números (acumulador y contador) y calcule el promedio, en caso de que haya división por cero imprimir un mensaje de error y retornar 0.
    '''
    if contador > 0:
        promedio = acumulador / contador
        return promedio
    else:
        return 'no se puede dividir por cero'


def area_rectangulo(base:int, altura:int)->int:
    '''
    2.Crear una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.
    '''
    area = base * altura
    return area

def verificar_par(numero:int)->bool:
    '''
    3.Crear una función que verifique si un número es par o no, devuelve True si es par, y False si es impar
    '''
    if numero % 2 == 0:
        return True
    else:
        return False


def verificar_primo(numero:int)->bool:
    '''
    4.Crear una función que verifique si un primo o no, devuelve True si es primo, False si no lo es
    '''
    flag = True
    num = int(input('ingrese numero: '))

    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    if flag and num > 1:
        return True
    else:
         return False
    
def maximo_numero(num1:int,num2:int,num3:int)->int:
    '''
    5.Crear una función qué encuentre el máximo entre tres números. Debe aceptar tres argumentos y retornar el número más grande.
    '''
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return num1 # son las 3 iguales
    

def minimo_numero(num1:int,num2:int,num3:int)->int:
    '''
    6.Crear una función qué encuentre el mínimo entre tres números. Debe aceptar tres argumentos y retornar el número más chico.
    '''
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    elif num3 < num1 and num3 < num2:
        return num3
    else:
        return num1 # son las 3 iguales

def multiplicacion(num1:int,num2:int)->int:
    '''
    7. Crear una función qué se encargue de multiplicar dos números, la misma debe recibir como parámetro dos números y retornar el resultado.
    '''
    r = num1 * num2
    return r 


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