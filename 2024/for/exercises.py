

def ascending_numbers():
    '''
    1. show ascending numbers from 1 to 10
    '''
    array = []
    for i in range(1,11):
        array.append(i)
    return array
# print(ascending_numbers())

def descending_numbers():
    '''
    2. show descending numbers from 10 to 1
    '''
    array = []
    for i in range(10,0,-1):
        array.append(i)
    return array
# print(descending_numbers())

def ascending_acording_number():
    '''
    3. Enter a number. Display numbers from 0 to the number entered.
    '''
    array = []
    number = int(input('Enter the number: '))
    while number < 0:
        number = int(input('Must be greater than 0: '))
    for i in range(0, number+1):
        array.append(i)
    return array
# print(ascending_acording_number())

def multiply_number():
    '''
    4. Enter a number and display the multiplication table for that number. 
    '''
    acumulate=''
    number = int(input('Enter the number: '))
    for i in range(0,11):
        acumulate += f'\n{number} x {i} = {number*i}'
    return acumulate
# print(multiply_number())

def up_to_ten_numbers():
    '''
    5. A maximum of 10 numbers are entered or until the user enters the number 0. Show the sum and average of all numbers.
    '''
    array = []
    for i in range(0,10):
        number = int(input('Enter the number: '))
        array.append(number)
        question = input('Do you wish continue?(yes=1,no=0): ')
        while question.isalpha():
            question = input('Enter a number: 0 or 1 (yes=1,no=0): ')
        question = int(question)
        if question == 0:
            break
    return array

# print(up_to_ten_numbers())

def multiples_three():
    '''
    6. Print numbers multiples of 3 between 1 and 10
    '''
    array = []
    for i in range(1,11):
        if i % 3 == 0:
            array.append(i)
    return array
# print(multiples_three())

def number_to_fifty():
    '''
    7. Show the even numbers from the unit up to the number 50.
    '''
    array = []
    number = int(input('Enter the number: '))
    while number > 50:
        number = int(input('the number must less than 50: '))
    for i in range(number,51):
        if i % 2 == 0:
            array.append(i)
    return array
# print(number_to_fifty())

def pyramid_of_numbers():
    '''
    8. Show a pyramid of numbers
    example: 5
    1
    12
    123
    1234
    12345    
    '''
    number = int(input('Enter the number : '))
    acumulate = ''

    for i in range(1,number+1):
        acumulate += str(i)
        print(acumulate)


def show_divisor_number():
    '''
    9. Enter a number. Show all divisors from 1 to the number entered. Display the number of divisors found.
    '''
    array = []
    number = int(input('Enter the number: '))
    for i in range(1,number+1):
        if number % i == 0:
            array.append(i)
    return array

def show_prime_number():
    '''
    Enter a number. Determine whether the number is prime or not.
    '''
    prime = True
    number = int(input('Enter the number: '))
    if number <= 1:
        prime = False
    else:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                prime = False
    return prime
    
def show_primes_numbers():
    primes = []
    number = int(input('Enter the number: '))
    for i in range(1,number+1):
        prime = True
        if i <= 1:
            prime = False 
        else:
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    prime = False
        if prime == True:
            primes.append(i)
    return primes
            
print(show_primes_numbers())

