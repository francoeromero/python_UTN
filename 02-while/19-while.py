# Dada una lista de números, imprimir todos los números que son mayores que el número anterior en la lista.

numeros = range(0, 11)
i = 0
flag = 0
while(i < len(numeros)):
    if(flag == 0):
        mayor = i 
        flag = 1
    elif(i > mayor):
        mayor = i
    i += 1
print("El numero mayor de la lista es: ", mayor)

# # segun chat gpt
# numeros = [1, 5, 2, 6, 3, 8, 4, 9]
# i = 1

# while i < len(numeros):
#     if numeros[i] > numeros[i-1]:
#         print(numeros[i])
#     i += 1
