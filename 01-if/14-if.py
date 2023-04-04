# Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima "El número es múltiplo de 4 y de 6" si el número es múltiplo de 4 y de 6, o "El número no es múltiplo de 4 y de 6" si el número no es múltiplo de 4 y de 6.

n_ingresado = input("Ingresa un numero: ")
n = int(n_ingresado)
if(n % 4 == 0 and n % 6 == 0):
    print("El numero es multiplo de 4 y de 6")
else:
    print("No es multiplo de 4 y de 6")