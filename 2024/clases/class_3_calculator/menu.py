from functions import * 

def menu():
    a = None
    b = None
    while True:
        print('\n MENU CALCULATOR \n 1. Enter the first operand \n 2. Enter the second of operand \n 3. Calculate all operations \n 4. Report results \n 5. Exit')

        option = input('Enter a option: ')
        while not option.isdigit():
            option = input('Enter a option correctly: ')
        option = int(option)

        if option == 1:
            a = enter_first_operand()
        elif option == 2:
            b = enter_second_operand()
        elif option == 3:
            if a == None or b == None:
                print('You must enter a value to a and b')
            else:
                result_sum = calculate_addition(a,b)
                result_subtraction = calculate_subtract(a,b)
                result_division=calculate_division(a,b)
                result_multiplication = calculate_multiplication(a,b)
                result_power = calculte_power(a,b)
                result_remainder = calculate_remainder(a,b)
                result_factorial = calculate_factorial(a)
        elif option == 4:
            if a == None or b == None:
                print('You must enter a value to a and b')
            else:
                print(f'A) The result of the sum of a and b is {result_sum}')
                print(f'B) The result of the subtraction of a and b is {result_subtraction}')
                print(f'C) The result of the division of a and b is {result_division}')
                print(f'D) The result of the multiplication of a and b is {result_multiplication}')
                print(f'E) The result of the power of a and b is {result_power}')
                print(f'F) The result of the remainder of a and b is {result_remainder}')
                print(f'G) The result of the factorial of a and b is {result_factorial}')
        elif option == 5:
            print('Exiting.. ')
            break
        else:
            print('Invalide option, enter numbers from 1 to 5: ')
menu()