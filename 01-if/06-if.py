#Escribir un programa que le pida al usuario que ingrese su nombre y su edad, y luego imprima "Puedes votar" si la edad es mayor o igual a 18 y menor o igual a 65, o "No puedes votar" si la edad es menor a 18 o mayor a 65.


nombre_ingresado = input("Ingrese su nombre: ")
edad_ingresada = input("Ingrese su edad: ")
edad = int(edad_ingresada)
if(not(edad < 17 or edad > 66)):
    print("Hola {0} te comento que si puedes votar porque tu edad es {1}".format(nombre_ingresado, edad))
else:
    print("Hola {0} te comento que lamentablemente no puedes votar porque tu edad es {1}".format(nombre_ingresado, edad))






# def votacion():
#     nombre = input("Ingrese su nombre: ")
#     nombre = str(nombre)
#     edad = input("Ingrese su edad: ")
#     edad = int(edad)
#     if not(edad < 17 or edad > 64):
#         print("Puedes votar {0} porque tienes {1}".format(nombre, edad))
#     else:
#         print("No puedes votar {0} porque tienes {1}".format(nombre, edad))
# votacion()