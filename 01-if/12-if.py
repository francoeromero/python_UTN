# Escribir un programa que le pida al usuario que ingrese dos números enteros, y luego imprima "El primer número es positivo" si el primer número es mayor que cero, "El segundo número es positivo" si el segundo número es mayor que cero, o "Ambos números son negativos" si los dos números son negativos

primer_numero_ingresado = input("Ingrese un numero: ")
primer_numero = int(primer_numero_ingresado)
segundo_numero_ingresado = input("Ingrese un numero: ")
segundo_numero = int(segundo_numero_ingresado)
if(primer_numero > -1):
    print("El primer numero es positivo")
elif(segundo_numero > -1):
    print("El segundo numero es positivo")
if(primer_numero < 0 and segundo_numero < 0):
    print("Ambos son negativos")
