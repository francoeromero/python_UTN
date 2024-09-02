'''
Calcular todas las operaciones (No se puede acceder si no se ingresaron
los dos operandos)
a) Calcular la suma (A+B)
b) Calcular la resta (A-B)
c) Calcular la división (A/B)
d) Calcular la multiplicación (A*B)
e) Calcular potencia entre (A ** B)
f) Calcular resto entre (A % B)
g) Calcular el factorial (A!)

'''

def enter_first_operand()->int:
    '''
    Documentation:
    This function request the first operand for calculate 
    '''
    number = input('Enter the first operand: ')
    while not number.isdigit():
        number = input('Enter correctly the first operand: ')
    number = int(number)
    return number

def enter_second_operand()->int:
    '''
    Documentation:
    This function request the second operand for calculate 
    '''
    number = input('Enter the second operand: ')
    while not number.isdigit():
        number = input('Enter correctly the second operand: ')
    number = int(number)
    return number

def calculate_addition(num1:int,num2:int)->int:
    '''
    Documentation:
    This function calculates the sum of two numbers
    '''
    return num1 + num2

def calculate_subtract(num1:int,num2:int):
    '''
    Documentation:
    This function calculates the subtract of two numbers
    '''
    return num1 - num2

def calculate_division(num1:int,num2:int):
    '''
    Documentation:
    This function calculates the division of two numbers
    '''
    if num2 == 0:
        return 'cannot be divide by zero'
    else:    
        return num1 / num2

def calculate_multiplication(num1:int,num2:int):
    '''
    Documentation:
    This function calculates the division of two numbers
    '''
    return num1 * num2

def calculte_power(num1:int,num2:int):
    '''
    Documentation:
    This function calculates the power between two numbers
    '''
    return num1 ** num2

def calculate_remainder(num1:int, num2:int):
    '''
    Documentation:
    This function calculates the remainder between two numbers
    '''
    if num2 == 0:
        return 'cannot be divide by zero'
    else:
        return num1 % num2

def calculate_factorial(num1:int):
    '''
    Documentation:
    This function calculates the factorial between two numbers
    '''
    result = 1 
    for i in range(1, num1+1):
        result *= i
    return result