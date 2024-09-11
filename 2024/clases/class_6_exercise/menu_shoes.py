'''
En un local de venta de zapatillas, se necesita desarrollar un programa para llevar un
registro de las compras realizadas durante toda una semana. El programa debe permitir al
usuario ingresar las compras diarias y calcular ciertas estadísticas al final de la semana.
Funcionalidades del Programa:

1. Registro de Ingresos: El usuario podrá guardar en una única lista los ingresos totales
realizados durante cada día de la semana.
2. Análisis de Datos:
● Determinar el día con más ingresos.
● Determinar el día con menos ingresos.
● Calcular el promedio de ingresos en la semana.
● Calcular el total de ingresos en la semana.
● Calcular el promedio de ingresos en días laborables (de lunes a viernes) y en
días del fin de semana (sábado y domingo).
● Calcular el día con la mayor variación en los ingresos respecto al día anterior.
3. Muestra de datos: Una vez calculados todos los datos del punto 2, se deberán
imprimir en pantalla

'''
from functions_shoes import *

def menu():
    weekly_shopping = []
    while True:
        print('WELCOME TO THE SHOE STORE')
        print('\n 1. Weekly revenue register \n 2. Analyze data \n 3. Data sample')
        option = input('Enter a option: ')
        # validate
        while not option.isdigit() or int(option) > 3:
            option = input('Enter a option correctly: ')
        option = int(option)

        # options a
        if option == 1:
            days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
            for i in range(len(days)):
                amount = input(f'Enter the shopping day of {days[i]}: ')
                # validate
                while amount.isalpha() or int(amount)<0:
                    amount = input(f'Enter correctly the shopping day of {days[i]}: ')
                amount = int(amount)  
                weekly_shopping.append(amount)

        elif option == 2:
            if weekly_shopping == []:
                print('You must first enter the number 1 for register the revenue of week')
            else:
                day_with_most_revenue = most_revenue(weekly_shopping)
                day_with_least_revenue = least_revenue(weekly_shopping)           
                average_revenue_weekly = average_week(weekly_shopping)
                total_revenue_weekly = total_revenue(weekly_shopping)
                average_working_days = average_daysWork(weekly_shopping)
                average_weekend_days = average_weekend(weekly_shopping)
                
        elif option == 3:
            if weekly_shopping == []:
                print('You must first enter the number 1 for register the revenue of week')
            else:
                print(f'\n 1. The day with the most revenue is {day_with_most_revenue}')
                print(f'2. The day with the least revenue is {day_with_least_revenue}')
                print(f'3. The average revenue weekly is {average_revenue_weekly}')
                print(f'4. The total revenue weekly is {total_revenue_weekly}')
                print(f'5. The average working of days is {average_working_days}')
                print(f'5. The average weekend of days is {average_weekend_days}')
                weekly_shopping == []
menu()