def show():
    # get value
    age = int(input('Enter age: '))
    if age == 15:
        message = 'pretty girl'
    else :
        message = 'mistake'

def older():
    # get value 
    age = int(input('Enter age: '))
    if age > 18:
        message = 'you are older'
    elif age < 18:
        message = 'you are not older'

    return message


# variable = valor_si_verdadero if condición else valor_si_falso

def older_():
    # get value 
    age = int(input('Enter age: '))
    message = 'pretty girl' if age == 15 else 'girl' if age == 18 else 'girl' if age > 18 else 'error'
    return message

