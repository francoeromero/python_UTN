# Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
# adolescente (entre 13 y 17 años) o niño (menor a 13 años).

edad_ingresada = input("Ingrese su edad: ")
edad = int(edad_ingresada)
if(edad > 17):
    print("mayor de edad")
elif(not(edad < 13 or edad > 17)):
    print("Adolescente")
else:
    print("niño")

numero = input("Ingrese numero: ")
while(numero != 0):
    numero = input("ERROR! ")