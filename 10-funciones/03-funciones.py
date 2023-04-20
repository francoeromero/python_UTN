# Crear una función que calcule el descuento aplicado a un producto. Recibe dos parámetros (precio original y precio con descuento) y devuelve el porcentaje de descuento aplicado.

def calculo_descuento(precio_original, precio_con_descuento):
    porcentaje_aplicado = 100 - ((precio_con_descuento * 100)/precio_original)
    return porcentaje_aplicado
print(calculo_descuento(10,8), "%")

"""
precio original _____ 100%
precio descuento _____ x %

"""