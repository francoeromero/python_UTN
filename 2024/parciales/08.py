'''
Ej 1

En una hamburguesería el cajero debe ir cargando los pedidos de los clientes.
Los datos que se tienen que ingresar son:
Nombre, Apellido, edad.

Que tipo de hamburguesa (simple, doble o veggie), cantidad de hamburguesas. 
La simple vale 125, 
la doble 185 y 
la veggie 145.
Esto se debe cargar hasta que el cajero decida.
Al final, se deberá presentar:

A)Cuál fue el tipo de hamburguesa más comprada.

B)Cual fue el promedio de compra por tipo de hamburguesa.

C)El nombre y apellido de la persona que realizó la compra más barata.

'''

next = True
acumulate_quantity_burger = 0
acumulate_amount = 0
flag = 0
while next:

    name_client = input('Enter the name of client: ')
    while name_client.isdigit():
        name_client = input('Enter the name of client correctly: ')

    last_name_client = input('Enter the last name of client: ')
    while last_name_client.isdigit():
        last_name_client = input('Enter the last name of client correctly: ')
        
    age_client = input('Enter age of client: ')
    while age_client.isalpha() or int(age_client) < 0:
        age_client = input('Enter age correctly: ')
    age_client = int(age_client)

    type_burger = input('Enter the type of hamburger(simple/double/veggie): ')
    while type_burger != 'simple' and type_burger != 'double' and type_burger != 'veggie':
        type_burger = input('Enter correctly the type of hamburger(simple/double/veggie): ')
    
    quantity_burger = input('Enter how many burger do you want? ')
    while quantity_burger.isalpha() or int(quantity_burger) < 0:
        quantity_burger = input('Enter correctly how many burger do you want: ')
    quantity_burger = int(quantity_burger)

    if type_burger == 'simple':
        amount = quantity_burger * 125
    elif type_burger == 'double':
        amount = quantity_burger * 185
    elif type_burger == 'veggie':
        amount = quantity_burger * 145
    # A
    if flag == 0:
        most_bought = amount
        cheapest_bought = amount
        flag = 1
    elif amount > most_bought:
        most_bought = amount
        type_most_bought = type_burger
    # C
    elif amount < cheapest_bought:
        cheapest_bought = amount
        name_cheapest = name_client
        last_name_cheapest = last_name_client

    # B
    acumulate_amount += amount
    acumulate_quantity_burger += quantity_burger

    next = input('Do you wish continue?(y/n):')
    if next != 'y':
        next = False
# B
average_amount = acumulate_amount / acumulate_quantity_burger
