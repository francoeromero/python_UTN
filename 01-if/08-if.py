# Escribir un programa que le pida al usuario que ingrese un número entero positivo, y luego imprima "El número es un cuadrado perfecto" si el número es un cuadrado perfecto, o "El número no es un cuadrado perfecto" si el número no es un cuadrado perfecto.

def cuadrado_perfecto():
    numero = input("Ingrese un numero: ")
    numero = int(numero)
    raiz = int(numero ** 0.5)
    if raiz * raiz == numero:
        print("El numero es un cuadrado perfecto")
    else:
        print("El numero NO es un cuadrado perfecto")
cuadrado_perfecto()