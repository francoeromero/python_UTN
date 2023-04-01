# Escribir un programa que le pida al usuario que ingrese su nombre, y luego imprima "Hola [nombre]" si el nombre ingresado es "Juan", "María" o "Pedro", o "Hola desconocido" si el nombre ingresado no es uno de esos tres.


nombres = ["juan", "maria", "pedro"]
nombre_ingresado = input("Ingrese un nombre: ")
if(nombre_ingresado == nombres[0]):
    print("Hola {0}!".format(nombres[0]))
elif(nombre_ingresado == nombres[1]):
    print("Hola {0}!".format(nombres[1]))
else:
    print("Hola desconocido!")













# def saludador():
#     nombre = input("Ingrese su nombre juan, maria, pedro: ")
#     nombre = nombre.lower()
#     if nombre == "juan":
#         print("Hola Juan!")
#     elif nombre == "maria":
#         print("Hola Maria!")
#     elif nombre == "pedro":
#         print("Hola Pedro!")
#     else:
#         print("Hola desconocido!")
# saludador()