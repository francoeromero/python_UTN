# Escribir un programa que le pida al usuario que ingrese un número entero positivo, y luego imprima "El número ingresado es positivo" si el número es mayor que cero, o "El número ingresado es cero o negativo" si el número es menor o igual a cero
def mostrar():
    numero = input("Ingrese un numero: ")
    numero = int(numero)
    if(numero > 0):
        print("El numero es positivo")
    else:
        print("El numero es cero o negativo")
mostrar()