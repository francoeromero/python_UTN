'''
Ejercicio Integrador 01
La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
contagio, de cada una debe obtener los siguientes datos:
1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
1000 unidades)
4. La marca y el Fabricante.
Se debe informar lo siguiente:
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total.
'''

products = 5
flag_a = 0
flag_b = 0
sum_soaps = 0
for i in range(0,products):
    type_product = input('Enter the type of product(chinstrap/soap/alcohol): ').lower()
    while type_product != 'chinstrap' and type_product != 'soap' and type_product != 'alcohol':
        type_product = input('Only we have chinstrap/soap/alcohol: ').lower()

    price_product = input('Enter the price of product: (from 100 to 300): ')
    while price_product.isalpha() or int(price_product) < 100 or int(price_product)> 300:
        price_product = input('Enter price correctly (from 100 to 300): ')
    price_product = int(price_product)

    quantity_products = input('Enter the number of products: ')
    while quantity_products.isalpha() or int(quantity_products) < 0 or int(quantity_products) > 1000:
        quantity_products = input('Enter the quantity correctly, cannot exceed 1000: ')
    quantity_products = int(quantity_products)

    brand_product = input('Enter the brand of product: ')
    while brand_product.isdigit() :
        brand_product = input('Enter correctly the brand of product: ')

    fabric_product = input('Enter the fabric of product: ')
    while fabric_product.isdigit() :
        fabric_product = input('Enter correctly the fabric of product: ')

    if type_product == 'chinstrap':
        if flag_a == 0 or price_product > most_expensive_chinstrap:
            most_expensive_chinstrap = price_product
            quantity_most_expensive_chinstrap = quantity_products
            fabric_most_expensive_chinstrap = fabric_product
            flag_a = 1
    elif type_product == 'soap':
        sum_soaps += quantity_products

    if flag_b == 0 or quantity_products > more_products:
        more_products = quantity_products
        fabric_more_products = fabric_product
        flag_b = 1

print(f'a) Quantity of the most expensive chinstrap: {quantity_most_expensive_chinstrap}')
print(f'a) Manufacturer of the most expensive chinstrap: {fabric_most_expensive_chinstrap}')
print(f'b) Manufacturer with more products: {fabric_more_products}')
print(f'c) Total number of soaps: {sum_soaps}')
