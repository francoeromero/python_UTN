# Dada una lista de números, imprimir todos los números que son múltiplos de 3.

numeros = range(0, 20)
i = 0
while(i < len(numeros)):
    if(i > 2 and numeros[i] % 3 == 0):
        print(numeros[i])
    i += 1