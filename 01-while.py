# Dado un número entero n, imprimir todos los números desde n hasta 1 en orden descendente.

numero = input("Ingrese un numero: ")
numero_entero = int(numero)

while(numero_entero > 1):
    numero_entero = numero_entero - 1
    print(numero_entero)

numero = input("Ingrese un numero: ")
numero_entero = int(numero)
while(numero_entero < 10):
    numero_entero = numero_entero + 1
    print(numero_entero)