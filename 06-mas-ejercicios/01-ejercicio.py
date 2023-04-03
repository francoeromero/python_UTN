# Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
# sueldo para esa persona.

nombre = input("Ingrese un nombre: ")
sueldo_ingresado = input("Ingrese su sueldo: ")
sueldo = float(sueldo_ingresado)
aumento = sueldo * 0.1
sueldo_incrementado = sueldo + aumento
print("Señor {} tenia un sueldo {} y tiene un incremento de {} y en total seria {}".format(nombre, sueldo, aumento, sueldo_incrementado))