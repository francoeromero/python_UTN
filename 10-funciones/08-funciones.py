# Crear una función que verifique si un número es par o impar. Recibe un número como parámetro y devuelve True si es par o False si es impar.

def par_o_impar(num):
    if(num % 2 != 0):
        return "es impar"
    else:
        return "es par"
print(par_o_impar(3))

def es_par(num):
    if(num % 2 == 0):
        return True
    else:
        return False
print(es_par(3))