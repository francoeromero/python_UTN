'''
metodos de ordenamiento
Listas simples:
 1- Realizar una función que ordene una lista de entero en orden ascendente o
 descendente dependiendo de un parámetro que se le envíe, la función debe retornar
 la cantidad de cambios que se realizaron.

 2- Realizar una función que ordene una lista de nombres de la A-Z o viceversa
 dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad
 de cambios que se realizaron.

 3- Similar a la función anterior, se debe realizar otra que ordene una lista de
 nombres por su largo, de manera ascendente o descendente, la función debe
 retornar la cantidad de cambios que se realizaron

 Matrices:
 4- Ordenar una matriz de nombre-apellido de la A-Z o viceversa dependiendo de un
 parámetro que se le envíe, por otro lado, la función deberá recibir otro parámetro
 para indicar si la prioridad de ordenamiento la tendrá el nombre o el apellido

'''
from functions_sort import *
numbers = [2,6,5,9,3,15,29,21,4]
students = ['fran','ezequiel','katherine','carlos']
students_name_lastname = [
    ['franco','rodriguez'],
    ['ezequiel','gomez'],
    ['alan','alarcon']
    ]
while True:
    print('\n ORDENING METHODS \n1.NUMERICAL ORDER\n2.ALPHABETIC ORDER\n3.LONGITUDINALLY ORDER\n4.ORDER OF LIST BY NAME OR LASTNAME\n5. Exiting the system')
    option = int(input('Enter a option: '))
    print('-----------------------------------------------------------------')
    match option:
        case 1:
            print('NUMERICAL ORDER')
            print(f'The number of ordinance amendments: {sort_array(numbers,True)}')
        case 2:
            print('ALPHABETIC ORDER')
            print(f'The number of ordinance amendments: {sort_names_alphabetically(students)}')
        case 3:
            print('LONGITUDINALLY ORDER')
            print(f'The number of ordinance amendments: {sort_names_length(students)}')
        case 4:
            print('ORDER OF LIST BY NAME OR LASTNAME')
            print(f'{sort_name_lastname(students_name_lastname,'lastname')}')
        case 5:
            print('exiting the system')
            break
