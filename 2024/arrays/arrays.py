
'''
1. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
'''

def average_array(array:list):
    acumulater = 0
    for i in range(len(array)):
        acumulater += array[i]
    average = acumulater / len(array)
    return average

'''
2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos. En caso de no haber números positivos validar división por cero
'''

def average_positives(array:list):
    acumulater = 0
    counter = 0
    for i in range(len(array)):
        if array[i] > 0:
            acumulater += array[i]
            counter += 1
    average = acumulater / counter
    return average

'''
3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro
'''

def multiply_array(array:list):
    acumulater = 1
    for i in range(len(array)):
        acumulater *= array[i]
    return acumulater

'''
4.Escribir una función que reciba como parámetros una lista de enteros y retorne el índice del valor máximo encontrado (retornar un sólo índice, en caso de que haya más de un máximo el primero)

Ejemplo [2,5,5,3,1] -> Retorna el índice 1

'''

def maximum_value(array:list): 

    max = array[0]
    position = 0

    for i in range(len(array)):
        if i == 0 or array[i] > max:
            max = array[i]
            position = i
    return position

'''
5. Escribir una función que reciba como parámetros una lista de enteros y muestre el índice del valor máximo encontrado (no se tienen en cuenta si hay más de un máximo) Reutilizar la función anterior.Ejemplo [2,5,5,3,1] -> Imprime el índice  1 y su valor
'''
def only_maximum_value(array:list):
    position = maximum_value(array)
    value = array[position]
    answer = f'value: {value} position: {position}'
    return answer


'''
6.Escribir una función que reciba como parámetros una lista de enteros y retorne todos los índices del del valor máximo encontrado (Puede haber más de uno)

Ejemplo [2,5,5,3,1] -> Retorna el índice [1,2]

'''
def find_positions_values(array:list):

    positions = []
    position_max = maximum_value(array)
    value_max = array[position_max]

    for i in range(len(array)):
        if array[i] == value_max:
            positions.append(i)
    return positions


'''
7. Escribir una función que reciba como parámetros una lista de enteros y muestre la posición del valor máximo encontrado. Reutilizar la función anterior.

Ejemplo [2,5,5,3,1] -> Muestra tanto el índice 1 como el 2 y sus valores

'''

def find_positions_and_numbers(array:list):
    positions = find_positions_values(array)
    numbers = []
    for i in range(len(positions)):
        string = f'value: {array[positions[i]]} position: {positions[i]}'
        numbers.append(string)
    return numbers
   
'''
8. Definir y cargar una lista con 10 sueldos enteros aleatorios (utilizar random), entre ARS 350.000 y ARS 1.250.000. Calcular el porcentaje de personas que superan el salario promedio de estos mismos.
'''

import random

def salaries_random(min:int,max:int):
    salary = random.randint(min,max)
    return salary
 
def array_salaries_employees(number_employees:int):
    array_salaries = []
    min_salary = 350000
    max_salary = 1250000
    for i in range(number_employees):
        array_salaries.append(salaries_random(min_salary,max_salary))
    return array_salaries

def average_salaries(array:list):
    number_employees = len(array)
    salaries = array_salaries_employees(number_employees)
    sum = 0
    for i in range(len(salaries)):
        sum += salaries[i]
    average = sum / number_employees
    return average

def percentage_average_overrun(average:int, array:list):
    counter = 0
    for i in range(len(array)):
        if array[i] > average:
            counter += 1
    percentage = (counter * 100) / len(array)
    return percentage

def answer():
    array = array_salaries_employees(10)
    average = average_salaries(array)
    percentage = percentage_average_overrun(average, array)
    return percentage

print(answer())