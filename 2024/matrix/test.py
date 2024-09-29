lista_anidada = [[1,2,3,4],
                 [4,5,6,7],
                 [7,8,9,9]]

# lista anidadad [fila][columna]


# imprimir primeta columna
for i in range(len(lista_anidada)):
    print(lista_anidada[i][0])
# resultado
# 1
# 4
# 7

# imprimir todas las columnas 
for columna in range(len(lista_anidada[0])):#NUMERO DE COLUMNAS : 4
    for fila in range(len(lista_anidada)):#NUMERO DE FILAS : 3
        print(lista_anidada[fila][columna]) # imprime cada columna 

# imprimir en listas cada columna
array = []
for columna in range(len(lista_anidada[0])):
    column = []
    for fila in range(len(lista_anidada)):
        column.append(lista_anidada[fila][columna])
    array.append(column)
print(array)



