
'''
Realizar el algoritmo que permita ingresar los datos de una compra productos de la construccion, hasta que el cliente quiera:
Tipo validad("arena";"cal";"cemento")
Cantidad de bolsas,
Precio por bolsa (más de cero ),

Si compro más de 10 bolsas en total tenes 15% de descuento sobre el total a pagar.
Si compro más de 30 bolsas en total tenes 25% de descuento sobre el total a pagar.
a) El importe total a pagar , bruto sin descuento y...
b) el importe total a pagar con descuento(solo si corresponde)
d) Informar el tipo con mas cantidad de bolsas.
f) El tipo mas caro
'''

flag = 0
more_bags = 0
next = True
more_expensive_price = 0
while next:
    # material
    material = input('Enter the type of material you want to buy(sand/lime/cement): ').lower()
    while material != 'sand' and material != 'lime' and material != 'cement' or material.isdigit():
        material = input('Only we have sand or lime or cement(sand/lime/cement): ')
    # quantity
    quantity_bags = input('Enter numbers of bags: ')
    while int(quantity_bags) < 0 or quantity_bags.isalpha():
        quantity_bags = input('Minimum is one bag: ')
    quantity_bags = int(quantity_bags)
    # price
    price_bag = input('Enter the price of bag: ')
    while float(price_bag) < 0 or price_bag.isalpha():
        price_bag = input('You must write digits: ')
    price_bag = float(price_bag)

    # total price
    if quantity_bags > 10:
        total_price = quantity_bags * (price_bag * 0.85)
    elif quantity_bags > 30:
        total_price = quantity_bags * (price_bag * 0.75)
    else:
        total_price = quantity_bags * price_bag
    # price without discount
    total_price_without_discount = quantity_bags * price_bag

    if flag == 0:
        more_bags = quantity_bags
        more_expensive_price = total_price
        flag = 1 
    elif quantity_bags > more_bags:
        material_more_bags = material
        more_bags = quantity_bags
    elif total_price > more_expensive_price:
        more_expensive_price = total_price 
        more_expensive_price_material = material

    # continue?
    next = input('Do you wish continue?(y/n): ').lower()
    if next != 'y':
        next = False


