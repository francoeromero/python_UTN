# Escribir un programa que le pida al usuario que ingrese su nombre y su edad, y luego imprima "Eres adolescente" si la edad está entre 13 y 17 inclusive, "Eres adulto" si la edad está entre 18 y 64 inclusive, o "Eres adulto mayor" si la edad es mayor o igual a 65.

nombre = input("Ingrese su nombre: ")
edad_ingresada = input("Ingrese su edad: ")
edad = int(edad_ingresada)
if(not(edad < 12 or edad > 18)):
    print("Eres adolescente")
elif(not(edad < 17 or edad > 65)):
    print("Eres adulto")
elif(edad >= 65):
    print("Eres adulto mayor")