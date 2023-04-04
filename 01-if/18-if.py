# Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima "El número es par y es múltiplo de 3" si el número es par y es múltiplo de 3, o "El número no cumple ninguna de las dos condiciones" si el número no cumple ninguna de las dos condiciones.

n_ingresado = input("Ingrese un numero: ")
n = int(n_ingresado)
if(n % 3 == 0 and n % 2 == 0):
    print("El numero es par y es multiplo de 3")
else:
    print("El numero no cumple ninguna de las dos condiciones")