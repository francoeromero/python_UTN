# Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima "El número es divisible por 3 y por 5" si el número es divisible por 3 y por 5, o "El número no es divisible por 3 y por 5" si el número no es divisible por 3 y por 5.

n_ingresado = input("Ingrese un numero: ")
n = int(n_ingresado)
divisible_por_tres = n % 3
divisible_por_cinco = n % 5
if(divisible_por_tres == 0 and divisible_por_cinco == 0):
    print("El numero es divisible por 3 y por 5")
else:
    print("El numero no es divisible por 3 y 5")