# Escribir un programa que le pida al usuario que ingrese su edad, y luego imprima "Eres un niño" si la edad es menor a 12, "Eres un adolescente" si la edad está entre 12 y 17 inclusive, "Eres un adulto" si la edad está entre 18 y 64

edad_ingresada = input("Ingrese su edad: ")
edad = int(edad_ingresada)
if(edad < 12):
    print("Eres un niño")
elif(not(edad < 12 or edad > 17)):
    print("Eres un adolescente")
elif(not(edad < 17 or edad > 65)):
    print("Eres un adulto")