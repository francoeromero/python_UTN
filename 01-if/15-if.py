# Escribir un programa que le pida al usuario que ingrese un número entero positivo, y luego imprima "El número es primo" si el número es primo, o "El número no es primo" si el número no es primo.

n_ingresado = input("Ingrese un numero: ")
n = int(n_ingresado)
mensaje = "El numero es primo"

if(n <= 1):
    mensaje = "El numero No es primo"
else:
    for i in range(2, n):
        if n % i == 0:
            mensaje = "El numero No es primo"
print(mensaje)