
def detect_day(number:int):
    if number == 0:
        return 'Monday'
    elif number == 1:
        return 'Tuesday'
    elif number == 2:
        return 'Wednesday'
    elif number == 3:
        return 'Thursday'
    elif number == 4:
        return 'Friday'
    elif number == 5:
        return 'Saturday'
    elif number == 6:
        return 'Sunday'
    else:
        return 'Something went Wrong'

def most_revenue(array:list):
    flag = 0
    for i in range(len(array)):
        if flag == 0:
            max = array[i]
            position = i
            flag = 1
        elif array[i] > max:
            max = array[i]
            position = i
    return detect_day(position)

def least_revenue(array:list):
    flag = 0
    for i in range(len(array)):
        if flag == 0:
            min = array[i]
            position = i
            flag = 1
        elif array[i] < min:
            min = array[i]
            position = i
    return detect_day(position)

def average_week(array:list):
    acumulate = 0
    days_week = 7
    for i in range(len(array)):
        acumulate += array[i]
    average = acumulate / days_week
    return average

def total_revenue(array:list):
    acumulate = 0
    for i in range(len(array)):
        acumulate += array[i]
    return acumulate

def average_daysWork(array:list):
    acumulate = 0
    days_work = 5
    for i in range(days_work):
        acumulate += array[i]
    average = acumulate / days_work
    return average

def average_weekend(array:list):
    acumulate = 0
    lenght = len(array)
    for i in range(lenght - 2, lenght):
        acumulate += array[i]
    average = acumulate / 2    
    return average



'''
note : 
start (incluido): Es el valor inicial de la secuencia. Es el primer número que se incluirá en el rango. Si omites start, el rango comenzará en 0 por defecto.

stop (excluido): Es el valor final de la secuencia. Es importante notar que el número en stop no se incluye en la secuencia. El rango generará números hasta, pero sin incluir, este valor.
'''