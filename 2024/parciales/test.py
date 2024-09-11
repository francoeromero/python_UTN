edad = input('ingrese edad: ')
while edad.isalpha() or (int(edad) < 1 or int(edad) > 25):
    edad = input('ERROR! ingrese nuevamente: ')
edad = int(edad)

