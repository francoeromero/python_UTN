# Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima "El número ingresado es par" si el número es divisible por 2, o "El número ingresado es impar" si el número no es divisible por 2.


numero_ingresado = input("Ingrese un numero: ")
numero_ingresado_entero = int(numero_ingresado)
resto = numero_ingresado_entero % 2
if (resto == 0):
    print("El numero es par")
else:
    print("El numero es impar")















numero_texto = input("Ingrese numero: ")
# VALIDAR
numero_int = int(numero_texto)
resto = numero_int % 2
if resto == 0:
    print("par")
else:
    print("impar")




def numero_par():
    numero = input("Ingrese un numero: ")
    numero = int(numero)
    if numero % 2 == 0:
        print("EL numero ingresado es par")
    else:
        print("El numero ingresado es impar")
numero_par()

def numero_impar():
    numero = input("Ingrese un numero: ")
    numero = int(numero)
    if not(numero % 2 == 0):
        print("El numero es impar")
    else:
        print("El numero es par")
numero_impar()

