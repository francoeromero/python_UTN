'''
Desarrollar y probar el código en Entrada y salida Ej 1:

3- COPA PISTÓN:

Se deberá generar un programa para registrar las estadísticas de los 10 integrantes de una carrera de autos.
Se pedirá el ingreso de:

-Nombre
-Edad (mayor a 18)
-Nacionalidad del piloto (argentino, ingles, frances, brasilero, estadounidense)
-Cantidad de carreras ganadas (no pueden ser números negativos)
-Número del vehículo (no puede ser un número negativo)

Se necesita saber :

A) Nacionalidad del piloto más joven.
B) Cantidad de vehículos con número par.  x
C) Nombre del piloto con menos victorias y el número de auto impar.
D) Cantidad de pilotos mayores de 25 años con número de vehículo impar.
E) Nombre del piloto más joven con más victorias.
F) Nacionalidad del piloto más veterano con menos victorias.   
G) Promedio de edad de los pilotos que tiene un vehículo con número par.  x 
'''
members = 10
# a
flag_a = 0 
# b
number_even_vehicles = 0
# c
flag_c = 0
# d
count_age_more_25 = 0
# g
acumulate_age_even_vehicles = 0
count_age_even_vehicles = 0
for i in range(0,members):
    
    name_pilot = input('Enter names s pilot: ')
    while name_pilot.isdigit():
        name_pilot = input('Enter name s pilot correctly: ')

    age_pilot = input('Enter age of pilot: ')
    while not age_pilot.isdigit() or int(age_pilot) < 17:
        age_pilot = input('The pilot most be over 18 years old: ')
    age_pilot = int(age_pilot)

    nacionality_pilot = input('Enter the nationality of pilot(Argentine/English/French/Brazilian/American): ').lower()
    while nacionality_pilot != 'argentine' and nacionality_pilot != 'english' and nacionality_pilot != 'french' and nacionality_pilot != 'brazilian' and nacionality_pilot != 'american':
        nacionality_pilot = input('The pilot must be Argentine/English/French/Brazilian/American: ')
    
    quantity_races_won = input('Enter the number races won by the pilot: ')
    while not quantity_races_won.isdigit() or int(quantity_races_won) < 0:
        quantity_races_won = input('Enter numbers races won by pilot correctly: ')
    quantity_races_won = int(quantity_races_won)

    number_vehicle = input('Enter the number of vehicle: ')
    while not number_vehicle.isdigit() or int(number_vehicle) < 0:
        number_vehicle = input('Enter the number correctly: ')
    number_vehicle = int(number_vehicle)
    # A
    if flag_a == 0:
        youngest_age_pilot = age_pilot
        oldest_age_pilot = age_pilot
        nationality_youngest_pilot = nacionality_pilot
        youngest_more_victories = quantity_races_won
        oldest_less_victories = quantity_races_won
        nacionality_oldest_less_victories = nacionality_pilot
        flag_a = 1
    elif age_pilot < youngest_age_pilot:
        youngest_age_pilot = age_pilot
        nationality_youngest_pilot = nacionality_pilot
        # E) Nombre del piloto más joven con más victorias.
        if quantity_races_won > youngest_more_victories:
            youngest_more_victories = quantity_races_won
            name_youngest_more_victores = name_pilot
        # F)
    elif age_pilot > oldest_age_pilot:
        oldest_age_pilot = age_pilot
        if quantity_races_won < oldest_less_victories:
            oldest_less_victories = quantity_races_won
            nacionality_oldest_less_victories = nacionality_pilot

    if number_vehicle % 2 == 0:
        # pares / even
        number_even_vehicles += 1
        acumulate_age_even_vehicles += age_pilot
        count_age_even_vehicles += 1
        continue
    else:
        # impares / odd
        # C)
        if flag_c == 0:
            least_numbers_victories = quantity_races_won
            name_least_numbers_victories = name_pilot
            flag_c = 1
        elif quantity_races_won < least_numbers_victories:
            least_numbers_victories = quantity_races_won
            name_least_numbers_victories = name_pilot
        # D) Cantidad de pilotos mayores de 25 años con número de vehículo impar.
        if age_pilot > 25:
            count_age_more_25 += 1
# g
if count_age_even_vehicles > 0:
    average_age_pilots = acumulate_age_even_vehicles / count_age_even_vehicles
else:
    average_age_pilots = 0
    
print(f'A) Nationality of the youngest pilot is: {nationality_youngest_pilot}')
print(f'B) Number of even numbered vehicles is: {number_even_vehicles}')
print(f'C) Name of the pilot with the least number of victories is : {name_least_numbers_victories}')
print(f'D) Number of pilots over 25 years old with an odd number vehicle is: {count_age_more_25}')
print(f'E) Name of the youngest pilot with the most victories is: {name_youngest_more_victores}')
print(f'F) Nationality of the oldest pilot with the less victories is: {nacionality_oldest_less_victories}')
print(f'G) The average of age pilots with even numbered vehicles is:  {average_age_pilots}')