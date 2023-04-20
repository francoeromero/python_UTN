# Crear una función que calcule el máximo común divisor de dos números. Recibe dos parámetros (números) y devuelve el máximo común divisor.

def mcd(a, b):
    if(b == 0):
        return a
    else:
        return mcd(b, a % b)
print(mcd(10, 10))