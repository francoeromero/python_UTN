lista_anidada = [[1,2,3,4],
                 [4,5,6,7],
                 [7,8,9,9]]

#dividir las columnas 

# columnas = []
# for i in range(len(lista_anidada[0])):
#     columna = []
#     for j in range(len(lista_anidada)):
#         columna.append(lista_anidada[j][i])
#     columnas.append(columna)


# inicializar una matriz
# ecuacion:
# fila = [numeroinicial] * cantidad_columnas

# matriz = []
# for i in range(3):
#     fila = [2] * 2
#     matriz += [fila]
# print(matriz)


# for i in range(3):
#     fila = [2] * 2
#     matriz.append(fila)
# print(matriz)


def inicializar_matriz(cantidad_filas:int,cantidad_columnas:int,numero_inicial:int):
    matriz = []
    for i in range(cantidad_filas):
        fila = [numero_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz
    
matriz_a = inicializar_matriz(2,5,1)
matriz_b = inicializar_matriz(2,5,2)


def sumar_matrices(primera_matriz:list,segunda_matriz:list):
    matriz_nueva = []
    for i in range(len(primera_matriz)): #filas
        columna = []
        for j in range(len(primera_matriz[0])): #columnas
            suma = primera_matriz[i][j] + segunda_matriz[i][j]
            columna.append(suma)
        matriz_nueva.append(columna)

    return matriz_nueva
print(f'matriz a: {matriz_a}')
print(f'matriz b: {matriz_b}')
print(sumar_matrices(matriz_a,matriz_b))

