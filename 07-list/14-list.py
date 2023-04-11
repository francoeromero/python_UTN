# Crea dos listas de 10 números enteros cada una y realiza una multiplicación de los elementos con el mismo índice en ambas listas.

numeros_uno = list(range(0, 11))
numeros_dos = list(range(0, 11))
resultados = []
for i in range(len(numeros_uno)):
    resultado = numeros_uno[i] * numeros_dos[i]
    resultados.append(resultado)
print(resultados)
