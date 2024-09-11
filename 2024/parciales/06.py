'''
Desarrollar y probar el código en Entrada y salida Ej 1:

2- Una concesionaria necesita realizar un sistema de ventas online, donde se calculará las preferencias de 11 clientes.


Los datos necesarios son:
-Nombre del cliente: (no puede contener números)
-Edad: (validar que sea mayor a 18 años)
-Tipo de vehículo:  (Auto - Camioneta - PickUp)
-Preferencia: (Nafta – Diesel - GNC)
-Precio por vehículo.
-Cantidad de vehículos.


Calcular y mostrar en un document.write:
A- A la compra más grande realizada, se le otorgará un 15% de descuento, mostrando el nombre del cliente y su edad.
B- La mínima cantidad de vehículos vendidos.
C- Cuántas camionetas a GNC se compraron.
D- El cliente más viejo que compró una PickUp Nafta.
E- El porcentaje de clientes que compraron Auto, Camioneta y PickUp.
'''

clients = 3
flag =0
most_expensive_vehicle = 0
client_most_expensive_vehicle = None
age_client_most_expensive_vehicle = None
min_quantity_vehicle = 0
count_van_gnc = 0
oldest_client_pickup = 0
discount = 0.85
discount_price_vehicle = None
for client in range(0, clients):
    # validation
    name_client = input('Enter the name of client: ')
    while name_client.isdigit():
        name_client = input('You must write the name of client, no numers: ')

    age_client = input('Enter the age of client: ')
    while int(age_client) < 0 or int(age_client) < 18 or age_client.isalpha():
        age_client = input('The age of client must be exceed 18 years old: ')
    age_client = int(age_client)

    type_vehicle = input('Enter the type of vehicle(car/van/pickup): ').lower()
    while type_vehicle.isdigit() or type_vehicle != 'car' and type_vehicle != 'van' and type_vehicle != 'pickup':
        type_vehicle = input('Only we have car or van or pickup: ').lower()
    
    preference = input('Enter the preference of vehicle (gasoline/disel/gnc): ').lower()
    while preference.isdigit() or preference != 'gasoline' and preference != 'disel' and preference != 'gnc':
        preference = input('We have only gasoline or disel or gnc: ').lower()

    price_vehicle = input('Enter the price of vehicle: ')
    while price_vehicle.isalpha() or float(price_vehicle) < 0:
        price_vehicle = input('Enter the price correctly: ')
    price_vehicle = float(price_vehicle)

    quantity_vehicle = input('Enter the quantity vehicle: ')
    while quantity_vehicle.isalpha() or int(quantity_vehicle) < 0:
        quantity_vehicle = input('Enter the quantity correctly: ')
    quantity_vehicle = int(quantity_vehicle)
    # A- A la compra más grande realizada, se le otorgará un 15% de descuento, mostrando el nombre del cliente y su edad.
    if flag == 0:
        most_expensive_vehicle = price_vehicle
        min_quantity_vehicle = quantity_vehicle
        oldest_client_pickup = age_client
        flag = 1
    elif price_vehicle > most_expensive_vehicle:
        discount_price_vehicle = price_vehicle * discount
        most_expensive_vehicle = price_vehicle
        client_most_expensive_vehicle = name_client
        age_client_most_expensive_vehicle = age_client
    # B- La mínima cantidad de vehículos vendidos.
    elif quantity_vehicle < min_quantity_vehicle:
        min_quantity_vehicle = quantity_vehicle
    # D- El cliente más viejo que compró una PickUp Nafta.
    elif age_client > oldest_client_pickup and type_vehicle == 'pickup':
        oldest_client_pickup = age_client
    # C- Cuántas camionetas a GNC se compraron.
    if type_vehicle == 'van' and preference == 'gnc':
        count_van_gnc += 1
    # E
    acumulate_car = 0
    acumulate_van = 0
    acumulate_pickup = 0
    acumulate_general = 0
    if type_vehicle == 'car':
        acumulate_car += quantity_vehicle
    elif type_vehicle == 'van':
        acumulate_van += quantity_vehicle
    elif type_vehicle == 'pickup':
        acumulate_pickup += quantity_vehicle
    acumulate_general += quantity_vehicle

percentage_car = (acumulate_car * 100) / acumulate_general
percentage_van = (acumulate_van * 100) / acumulate_general
percentage_pickup = (acumulate_pickup * 100) / acumulate_general

print(f'A) Price without discount: {most_expensive_vehicle}')
print(f'A) Price with discount: {discount_price_vehicle}')
print(f'A) Name of client the most expensive vehicle: {client_most_expensive_vehicle}')
print(f'A) Age of client s most expensive vehicle: {age_client_most_expensive_vehicle}')
print(f'B) Minimum quantity cars sold: {min_quantity_vehicle}')
print(f'C) Quantity gnc cars sold: {count_van_gnc}')
print(f'D) Age of the oldest client bought pickup: {oldest_client_pickup}')
print(f'E) The percentage of cars: {percentage_car}')
print(f'E) The percentage of van: {percentage_van}')
print(f'E) The percentage of pickup: {percentage_pickup}')