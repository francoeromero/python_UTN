def aumento():
    # pido dato
    numero = input("Ingrese un numero: ")
    # parseo 
    numero = float(numero)
    # aumento un 20 % 
    aumento = numero * 1.2
    # muestro
    print(aumento)
aumento()

def descuento():
    numero = input("Ingrese un numero: ")
    numero = float(numero)
    descuento = numero * 0.5
    print(descuento)
descuento()