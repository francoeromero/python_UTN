
# for fil in range(4):
#      col = 3
#      inicial = 2
#      print([inicial] * col)

matriz = [
    [4,7,1],
    [-2,5,9],
    [5,4,-4]
]

# for fil in range(len(matriz)):
#     print(matriz[fil])
columnas = []
for fil in range(len(matriz)):
    columna = []
    for col in range(len(matriz[fil])):
        columna.append(matriz[fil][col])
    columnas.append(columna)
print(columnas)