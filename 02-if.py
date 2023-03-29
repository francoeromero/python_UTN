# Escribir un programa que le pida al usuario que ingrese su edad, y luego imprima "Eres mayor de edad" si la edad es mayor o igual a 18, o "Eres menor de edad" si la edad es menor a 18.

def edad_ingresada():
    edad = input("Ingrese su edad: ")
    edad = int(edad)
    if edad > 17:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
edad_ingresada()