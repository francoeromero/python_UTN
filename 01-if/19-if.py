# Escribir un programa que le pida al usuario que ingrese su edad, y luego imprima "Eres mayor de edad" si la edad es mayor o igual a 18, "Eres adolescente" si la edad está entre 13 y 17 inclusive, o "Eres menor de edad" si la edad es menor que 13.

edad_ingresada = input("Ingrese un edad: ")
edad = int(edad_ingresada)
if(edad >= 18):
    print("Eres mayor de edad")
elif(not(edad < 13 or edad > 17)):
    print("Eres adolescente")
elif(edad < 13):
    print("Eres menor de edad")