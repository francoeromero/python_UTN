# Ejercicio 8:
# Dada la siguiente lista:
# [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29,
# 58] mostrar el número repetido

numeros = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58, 58] 
numeros_repetidos = [] 

######con for
for i in numeros:
    if(numeros.count(i) > 1 and i not in numeros_repetidos):
        numeros_repetidos.append(i)
print("Los numeros que se repiten son: ", numeros_repetidos)

# ##### con while
# i = 0
# while(i < len(numeros)):
#     num = numeros[i]
#     if((numeros.count(num) > 1) and (num not in numeros_repetidos)):
#         numeros_repetidos.append(num)
#     i += 1
# print("Los numeros que se repiten son: ", numeros_repetidos)

# ##### como saber cuando se repite
# lista = [ 1, 1, 1, 5, 6, 3]
# repeticion = lista.count(lista[3])
# print(repeticion)

