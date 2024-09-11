'''
En una veterinaria se busca imprementar un sistema de registro para llevar un seguimiento detallado de las mascotas atendidas en el establecimiento. El registro debera contener la siguiente informacion:
* DNI del dueño de la mascota
* Nombre de la mascota
* Edad de la mascota 
* Especie de la mascota
* Sexo de la mascota
* Peso de la mascota
* Fecha de la ultima visita
* Historial médico

El programa debe permitir al veterinario:
1- Registrar nuevas mascotas, ingresando todos los datos requeridos
2- Actualizar la informacion de una mascota en cada nueva visita, manteniendo un historial medico completo y actualizado

Ademas, se requiere que el sistema proporcione las siguientes funcionalidades:
1- Mostrar informacion completa de todas las mascotas: Esta funcion permitirá visualizar todos los datos registrados de todas las mascotas atendidas en la veterinaria. 

2- Mostrar información completa solo de las mascotas que superen el promedio de edad: Esta opcion mostrará unicamente los datos de las mascotas cuya edad supere el promedio de edad de todas las mascotas registradad.

3- Calcular el promedio de peso de todas las mascotas: Esta funcion calculara y mostrara el promedio de peso de todas las mascotas registradas en la veterinario.

4- Contar la cantidad de perros registrados: Permitirá obtener el numero total de perros registrados en el sistema

5- Identificar el tipo de mascota registrado: Esta funcion determinará cual es el tipo de mascota(perro, gato, ave, etc) que mas se ha registrado en la veterinaria.

'''

import datetime

# obtener la fecha de hoy
# date_today = datetime.date.today()
# cambiar el formato del mes
# custom_format = fecha_hot.strftime('%d/%m/%Y')  

pet_registration = [
    ['12345678','Luna', 3, 'Dog', 'Female', 8.5, '01/05/2024', 'Vacunación anual'],
    ['12345678', 'Max', 7, 'Cat', 'Male', 5.2, '28/04/2024', 'Control de pulgas'],
    ['12345678', 'Kiwi', 1, 'Dragon', 'Female', '88000', '02/05/2024', 'Recorte de alas'],
    ['12345678', 'Rocky', 5, 'Dog', 'Male', 12.1, '30/04/2024', 'Revision dental'],
    ['12345678', 'Coco', 2, 'Cat', 'Female', 4.8, '03/05/2024', 'Desparasitacion']
]
main_history = [['12345678', 'Rocky', '03/05/2024', 'Desparasitacion'],['12345678', 'Rocky', '03/05/2024', 'Desparasitacion']]

from functions_veterinary import *
while True:
    print('\n MENU VETERINARY \n 1. Register pet \n 2. Update information of the pet \n 3. show pets that exceed the average age of pets  \n 4. show only pets above average age \n 5. calculate the average number of pets \n 6. count number of dogs \n 7. Identify the most registered pet type \n 8. Exiting the system')
    option = int(input('Enter a option: '))
    match option:
        case 1:
            new_pet = register()
            pet_registration.append(new_pet)
            print(pet_registration)
        case 2:
            i = search_pet(pet_registration)
            if i == None:
                print('\n the pet does not registered')
            else:
                print('\n its was found! ')
                
                question = options('Do you want to check the history or update?(C/U): ', 'Enter correctly C(Check history) or U (update history): ', ['C','U'])
                if question == 'u':
                    update(pet_registration, i, main_history)
                    print(f'Updated history! \n {pet_registration[i]}')
                elif question == 'c':
                    print(show_history(pet_registration[i][1], main_history))

        case 3:
            average = average_age_pets(pet_registration)
            print(f'The average is : {average}')
            pets = pets_exceed_average(average, pet_registration)
            print(f'Pets that exceed average age of pets: \n{pets}')
        case 4:
            print('mostrar solo mascotas que superen promedio de edad')
        case 5:
            print('calcular el promedio de mascotas')
        case 6:
            print('contar cantidad de perros')
        case 7:
            print('identificar tipo de mascota mas registrado')
        case 8:
            print('saliendo del sistema')
            break
