# Ejercicio 6:
# Utilizar For
# Dada la siguiente lista:
# [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29,
# 58] mostrar el mayor.

numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
maximo = numeros[0]
# i = 0
# while(i < len(numeros)):
#     if(numeros[i] > maximo):
#         maximo = numeros[i]
#     i += 1
# print("El mayor es ", maximo)

for numero in numeros:
    if(numero > maximo):
        maximo = numero
print("El mayor es ", maximo)
