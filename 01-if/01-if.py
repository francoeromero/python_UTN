# Escribir un programa que le pida al usuario que ingrese un número entero positivo, y luego imprima "El número ingresado es positivo" si el número es mayor que cero, o "El número ingresado es cero o negativo" si el número es menor o igual a cero
# def mostrar():
#     numero = input("Ingrese un numero: ")
#     numero = int(numero)
#     if(numero > 0):
#         print("El numero es positivo")
#     else:
#         print("El numero es cero o negativo")
# mostrar()

#################################
numero_entero_ingresado = input("Escribe un numero entero positivo: ")
numero_entero = int(numero_entero_ingresado)
if (numero_entero > 0):
    print("El número ingresado es positivo")
else:
    print("El número ingresado es negativo o cero")