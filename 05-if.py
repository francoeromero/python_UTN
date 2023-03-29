# Escribir un programa que le pida al usuario que ingrese su nombre, y luego imprima "Hola [nombre]" si el nombre ingresado es "Juan", "María" o "Pedro", o "Hola desconocido" si el nombre ingresado no es uno de esos tres.

def saludador():
    nombre = input("Ingrese su nombre juan, maria, pedro: ")
    nombre = nombre.lower()
    if nombre == "juan":
        print("Hola Juan!")
    elif nombre == "maria":
        print("Hola Maria!")
    elif nombre == "pedro":
        print("Hola Pedro!")
    else:
        print("Hola desconocido!")
saludador()