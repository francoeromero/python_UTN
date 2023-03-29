#Escribir un programa que le pida al usuario que ingrese dos números enteros, y luego imprima "El primer número es mayor" si el primer número es mayor que el segundo, "El segundo número es mayor" si el segundo número es mayor que el primero, o "Los dos números son iguales" si los dos números son iguales.
"""
def quien_es_mayor():
    primer_numero = input("Ingrese el primer numero: ")
    primer_numero = float(primer_numero)
    segundo_numero = input("Ingrese el segundo numero: ")
    segundo_numero = float(segundo_numero)
    if primer_numero > segundo_numero:
        print("El primer numero es mayor")
    elif segundo_numero > primer_numero:
        print("El segundo numero es mayor")
    else:
        print("Los numeros son iguales")
quien_es_mayor()
"""
def mayor():
    primer_numero = input("Ingrese un numero: ")
    primer_numero = float(primer_numero)
    segundo_numero = input("Ingrese otro numero: ")
    segundo_numero = float(segundo_numero)
    el_numero_mas_grande = 0
    if primer_numero > segundo_numero:
        el_numero_mas_grande = primer_numero
        orden_numero = "primer numero"
    else:
        el_numero_mas_grande = segundo_numero
        orden_numero = "segundo numero"
    if primer_numero == segundo_numero:
        print("Los numeros son iguales")
    else:
        print("El numero mas grande es el {0} y el numero es {1}".format(orden_numero, el_numero_mas_grande))
mayor()      