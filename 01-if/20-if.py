# Escribir un programa que le pida al usuario que ingrese dos números enteros, y luego imprima "Los dos números son iguales" si los dos números son iguales, "El primer número es mayor" si el primer número es mayor que el segundo, o "El segundo número es mayor" si el segundo número es mayor que el primero.


primer_numero_ingresado = input("Ingrese un numero: ")
primer_numero = int(primer_numero_ingresado)
segundo_numero_ingresado = input("Ingrese un numero: ")
segundo_numero = int(segundo_numero_ingresado)
if(primer_numero == segundo_numero):
    print( "Los dos números son iguales")
elif(primer_numero > segundo_numero):
    print("El primer número es mayor")
elif(segundo_numero > primer_numero):
    print("El segundo numero es mayor")
    