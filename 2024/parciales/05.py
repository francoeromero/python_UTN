'''
/*
Desarrollar y probar el código en Entrada y salida Ej 1:

1- Un local de computación que se especializa en venta de insumos importados desea calcular ciertas métricas en base a las ventas de sus productos.

Se ingresa de cada venta: (Ingresa mínimo 6 ventas)
-Nombre del producto.
-Género: (Memorias – Discos – Motherboards)
-Tipo de Venta: (Online – Local)
-Importe: (No pueden ser números negativos ni mayor a los $45500)


Se pide:
A- La más barata de las “Motherboards” con su importe .
B- De la venta más cara, el nombre del producto.
C- El importe promedio del total.
D- La cantidad de ventas online que sean de “Discos” y cuesten menos de $945.

*/
'''
quantity_products = 6
flag = 0
next = True
cheapest_amount_motherboards = 0
name_cheapest_motherboard = None
most_expensive_sale = 0
sum_amount = 0
count_discs = 0
for i in range(0,quantity_products):
    product_name = input('Enter the name s product: ')
    while product_name.isdigit():
        product_name = input('No digits, write again: ')

    product_gender = input('Enter the gender s producto(Memory/Disk/Motherboards): ').lower()
    while product_gender != 'memory' and product_gender != 'disk' and product_gender != 'motherboards':
        product_gender = input('Write correct the gender(Memory/Disk/Motherboards): ')
    
    type_sale = input('Enter type of sale (local / online): ')
    while type_sale != 'local' and type_sale != 'online':
        type_sale = input('Write again (local / online): ')

    amount = input('Enter the amount: ')
    while amount.isalpha() or float(amount) < 0 or float(amount) > 45500:
        amount = input('The amount must not be negative or exceed 45500: ')
    amount = float(amount)
    # A- La más barata de las “Motherboards” con su importe .
    if flag == 0:
        cheapest_amount_motherboards = amount
        most_expensive_sale = amount
        flag = 1
    elif product_gender == 'motherboards' and amount < cheapest_amount_motherboards:
        cheapest_amount_motherboards = amount
        name_cheapest_motherboard = product_name
    # B
    elif amount > most_expensive_sale:
        most_expensive_sale = amount
    # C
    sum_amount += amount
    # D- La cantidad de ventas online que sean de “Discos” y cuesten menos de $945.
    if type_sale == 'online' and product_gender == 'disk' and amount < 945:
        count_discs += 1
# C
average_amount = sum_amount / quantity_products
print(f'A) The name of cheapest motherboard is: {name_cheapest_motherboard}')
print(f'and the amount of cheapest motherboard is: {cheapest_amount_motherboards}')
print(f'B) The most expensive sale is: {most_expensive_sale}')
print(f'C) The average amount is : {average_amount}')
print(f'D) The number of online sales discs with a value not exceeding 945 is: {count_discs}')