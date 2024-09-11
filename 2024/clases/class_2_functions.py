'''
Ejercicio 01: Escribe una función que calcule el área de un círculo. La función debe recibir
el radio como parámetro y devolver el área.

Ejercicio 02: Crea una función que verifique si un número dado es par o impar. La función
debe imprimir un mensaje indicando si el número es par o impar.

Ejercicio 03: Define una función que encuentre el máximo de tres números. La función
debe aceptar tres argumentos y devolver el número más grande.

Ejercicio 04: Diseña una función que calcule la potencia de un número. La función debe
recibir la base y el exponente como argumentos y devolver el resultado.

Nota: Todas las funciones deben estar probadas y se podrá acceder a cada una de
ellas mediante un menú de opciones.
'''


def calculate_area_circle(radio:int, pi=3.14):
    '''
    This function calculates the area of a circle
    '''
    result = pi * radio ** 2
    return result

def check_even_odd(number:int):
    '''
    This function checks whether the number entered is odd or even
    '''
    if number % 2 == 0:
        message = 'The number entered is even'
    else:
        message = 'The number entered is odd'
    return message

def maximum_three_numbers(number_one:int, number_two:int, number_three:int):
    '''
    This function finds the maximum of three numbers
    '''
    numbers = [number_one, number_two, number_three]
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

def power_number(base:int,exponent:int):
    '''
    This function finds the power of a number 
    '''
    return base ** exponent
