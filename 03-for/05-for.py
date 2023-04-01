# Dada una lista de números, imprimir el número más pequeño de la lista.

lista_numeros = list(range(5, 20))
numero_mas_pequeño = lista_numeros[3]
for i in lista_numeros:
    if(i < numero_mas_pequeño):
        numero_mas_pequeño = i
print("El numero mas pequeño es ", numero_mas_pequeño)