# Dada una lista de números, imprimir la cantidad de números pares en la lista.

# asi se haria en for sin imprimir pares
# numeros = range(1, 9)
# for i in numeros:
#     print(i)

numeros = range(1, 9)
i = 0
while(i <= numeros[-1]):
    if(i % 2 == 0):
        print(i)
    i += 1

