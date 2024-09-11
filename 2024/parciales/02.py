'''
Bienvenidos.
Realizar el algoritmo que permita iterar el ingreso de dos datos, una letra y un número entre -100 y 100 (validar) hasta que el usuario quiera e informar al terminar el ingreso por document.write:
a) La cantidad de números pares.
b) La cantidad de números impares.
c) La cantidad de ceros.
d) El promedio de todos los números positivos ingresados.
e) La suma de todos los números negativos.
f) El número y la letra del máximo y el mínimo.

'''
# variables
next = True
even_numbers = 0
odd_numbers = 0
zeros_numbers = 0
sum_even_numbers = 0
negative_numbers = 0
flag = 0
max_letter = ''
min_letter = ''
max_number = 0
min_number = 0

while next:
    # get values
    letter = input('Enter a letter: ').lower()
    while not letter.isalpha() or len(letter) != 1:
        letter = input('The letter must not be a number: ')

    number = int(input('Enter a number: '))
    while number < -100 or number > 100 or number.isalpha():
        number = int(input('The number must not be a letter: '))
    
    # calculate
    # a) cantidad de numeros pares
    if number % 2 == 0:
        even_numbers += 1
        sum_even_numbers += number
    # b) cantidad de numeros impares
    if number % 2 != 0:
        odd_numbers += 1
    # c) cantidad de zeros
    if number == 0:
        zeros_numbers += 1
    # e) cantidad de numeros negativos
    if number < 0:
        negative_numbers += 1

    # f) la letra con su numero max y min
    if flag == 0:
        max_number = number
        min_number = number
        flag = 1
    elif number > max_number:
        max_number = number
        max_letter = letter
    elif number < min_number:
        min_number = number
        min_letter = letter

    next = input('Do you wish continue? (y/n): ').lower()
    if next != 'y':
        next = False
# d) prmedio de todos los numeros positivos
if even_numbers > 0:
    average_even_numbers =  sum_even_numbers / even_numbers 
else:
    average_even_numbers = 0
# show result
print(f'a) Quantity even numbers: {even_numbers}')
print(f'b) Quantity odd numbers: {odd_numbers}')
print(f'c) Quantity zeros numbers: {zeros_numbers}')
print(f'd) Average even numbers: {negative_numbers}')
print(f'e) Quantity negative numbers: {negative_numbers}')
print(f'f) maximum letter: {max_letter}')
print(f'f) minimum letter: {min_letter}')
