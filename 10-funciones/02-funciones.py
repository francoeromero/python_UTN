# Crear una función que calcule el área de un círculo. Recibe un parámetro (radio) y devuelve el área del círculo.

def area_circulo(radio):
    # radio = input("Ingrese el radio del circulo: ")
    # radio = float(radio)
    resultado = 3.14*radio**2
    return resultado
print(area_circulo(5))

#### practica #####
"""
1- declarar la funcion, especificar los parametros para hacer calculos
2- dentro del cuerpo de la funcion instrucciones
3- usar return para devolver el resultado si es que la funcion es llamada
4- llamar ala funcion ingresando valores a sus parametros
"""

def area_cuadrado(lado):
    resultado = lado * lado
    return resultado
print(area_cuadrado(10))

def area_rectangulo(ancho, largo):
    resultado = ancho * largo
    return resultado # devuelve el resultado de la linea 20, que la llama
print(area_rectangulo(8, 20))
