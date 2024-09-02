'''
Arrays Unidimensionales
1. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el
promedio de todos los números.

2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el
promedio de los números positivos.

3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista
que recibe como parámetro.

4. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición
del valor máximo encontrado.

5. Escribir una función que reciba como parámetros una lista de enteros y muestre la/las
posiciones en donde se encuentra el valor máximo hallado.

6. Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista
de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe
reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente
reemplazo y luego retornar la cantidad total de reemplazos realizados

'''

def average_integers(array:list):
    '''
    1. Calculates the average of all the numbers in a array
    '''
    sum = 0
    for i in range(len(array)):
        sum = sum + array[i]

    average = sum / len(array)
    return average


def average_positives(array:list):
    '''
    2. Calculates the average of positives numbers in a array
    '''
    numbers_positives= 0
    sum = 0

    for i in range(len(array)):
        if array[i] > 0:
            sum = sum + array[i]
            numbers_positives += 1

    average = sum / numbers_positives
    return average



def product_array(array:list):
    '''
    3. Multiplies all numbers in a array
    '''
    product = 1
    for i in range(len(array)):
        product = product * array[i]
    return product


def find_position_max(array:list):
    '''
    4. Finds the position of the maximum number in a array
    '''
    flag = 0
    for i in range(len(array)):
        if flag == 0:
            max = array[i]
            position = i
            flag = 1
        elif array[i] > max:
            max = array[i]
            position = i
    return position

lista = [1,2,33,-3,-8,33]

# def find_positions_max(array:list):
#     '''
#     5. Positions maximum values
#     '''
#     flag = 0
#     positions_max = []
#     for i in range(len(array)):
#         if flag ==0:
#             max = array[i]
#             flag = 1
#         if array[i] > max:
#             max = array[i]
#             positions_max.append(i)
#         if max == array[i]:
#             positions_max.append(i)
#     return positions_max
# print(find_positions_max(lista))




names = ['fran','kati','fernando','fran']
def replace_name(array:list,name_to_replace:str,replace_name:str):
    '''
    Replaces name of an array
    '''
    count_replaces = 0

    for i in range(len(array)):
        if name_to_replace.lower() == array[i]:
            array[i] = replace_name.lower()
            count_replaces += 1
    print(array)
    return count_replaces

name = 'fran'
replace = 'franco'
print(replace_name(names,name,replace))
