# Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima "El número es negativo" si el número es menor que cero, "El número es cero" si el número es igual a cero, o "El número es positivo" si el número es mayor que cero.

n_ingresado = input("Ingrese un numero: ")
n = int(n_ingresado)
if(n < 0):
    print("El numero es negativo")
elif(n == 0):
    print("El numero es cero")
elif(n > -1):
    print("El numero es mayor que cero")
