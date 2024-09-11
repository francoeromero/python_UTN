'''
Bienvenidos.
Realizar el algoritmo que permita ingresar la marca del producto, el peso el cual debe ser entre 1 y 100 (validar),
la temperatura de almacenamiento(entre -30 y 30) hasta que el usuario quiera e informar al terminar el ingreso por document.write:
a) La cantidad de temperaturas pares.
b) La marca del producto más pesado
c) La cantidad de productos que se conservan a menos de 0 grados.
d) El promedio del peso de todos los productos.
f) El peso máximo y el mínimo.
'''

next = True

while next:

    # brand of the product
    brand_product = input('Enter brand of the product: ')

    # weight
    product_weight = int(input('Enter product weight: '))
    while product_weight < 1 or product_weight > 100:
        product_weight = int(input('ERROR! the product must weight between 1 and 100: '))

    # temperature
    temperature = int(input('Enter product temperature: '))
    while temperature < -30 or temperature > 30:
        temperature = int(input('ERROR, the temperature must betweeen -30 and 30: '))

    # a- cantidad de temperaturas pares
    even_temperature_counter = 0
    if temperature % 2 == 0:
        even_temperature_counter = even_temperature_counter + 1
    # b- la marca del producto mas pesado / f - maximum weight and minimum weight 
    flag = 0
    heavier_product = 0
    lighter_product = 0
    if flag == 0:
        heavier_product = product_weight
        lighter_product = product_weight
        flag = 1
    elif product_weight > heavier_product:
        heavier_product = product_weight
        brand_heaviest_product = brand_product
    elif product_weight < heavier_product:
        lighter_product = product_weight
    # c) La cantidad de productos que se conservan a menos de 0 grados.
    minus_zero_degrees_counter = 0
    if temperature < 0:
        minus_zero_degrees_counter = minus_zero_degrees_counter + 1
    # d) quantity and accumulator products
    products_weight_quantity = 0
    products_weight_accumulator = 0

    products_weight_quantity += 1
    products_weight_accumulator += product_weight



    next = input('Do you wish continue?(y/n) : ').lower()
    if next == 'y':
        next = False
    else:
        next = True
# d) El promedio del peso de todos los productos.
average_product_weight = products_weight_accumulator / products_weight_quantity
print(f'a) The quantity of temperature pairs is:  {products_weight_quantity}')
print(f'b) The brand of the haviest product is:  {brand_heaviest_product}')
print(f'c) The amount of products that are preserved at less than zero degrees is:  {minus_zero_degrees_counter}')
print(f'd) The average weight of all product is:  {average_product_weight}')
print(f'f) The maximum weight product is:  {heavier_product}')
print(f'f) The minimum weight product is:  {lighter_product}')