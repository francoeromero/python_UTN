

def numbers():
    number_one = int(input('Enter a number: '))
    number_two = int(input('Enter other number: '))
    return [number_one, number_two]

numbers = numbers()
def sum(numbers):
    return numbers[0] + numbers[1]

def subtraction(numbers):
    return numbers[0] + numbers[1]
def multiply(numbers):
    return numbers[0] * numbers[1]

def divide(numbers):
    return numbers[0] / numbers[1]