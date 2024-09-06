def ingresar_primer_operando()->int:
    a = input('Ingrese el primer operando: ')
    while a.isalpha() or a == '' or a == None:
        a = input('ERROR! debe ser un numero: ')
    a = int(a)
    return a

def ingresar_segundo_operando()->int:
    b = input('Ingrese el segundo operando: ')
    while b.isalpha() or b == '' or b == None:
        b = input('ERROR! debe ser un numero: ')
    b = int(b)
    return b

def calcular_suma(a,b)->int:
    '''Documentación:
    Esta funcion calcula la suma entre A y B
    '''
    r = a + b
    return r
def calcular_resta(a,b)->int:
    '''Documentación:
    Esta funcion calcula la resta entre A y B
    '''    
    r = a - b
    return r
def calcular_division(a,b)->int:
    '''Documentación:
    Esta funcion calcula la division entre A y B
    '''
    if b > 0:
        r = a / b
    else:
        r = 'no se puede dividir por cero'
    return r
def calcular_multiplicacion(a,b)->int:
    '''Documentación:
    Esta funcion calcula la multiplicacion entre A y B
    '''
    r = a * b
    return r

def calcular_potencia(a,b)->int:
    '''Documentación:
    Esta funcion calcula la potencia de A con B
    '''
    r = a ** b
    return r

def calcular_resto(a,b)->int:
    '''Documentación:
    Esta funcion calcula resto de A con B
    '''
    while b == 0:
        r = 'No se puede saber el resto de cero'
        return r
    r = a % b
    return r

def calcular_factorial(a)->int:
    '''Documentación:
    Esta funcion calcula el factorial de A
    '''
    if a == 0 or a == 1:
        r = 1
        return r
    else:
        for i in range((a-1), 0, -1):
            a = a * i
        r = a
        return r


def factorial(a):
    resultado = None
    if a == 0 or a == 1:
        return 1
    else:
        resultado = a * factorial(a - 1)
    return resultado
print(factorial(5))
