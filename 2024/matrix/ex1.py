

def inicializar_matriz(cant_filas:int,cant_columnas:int, valor_inicial:any):
    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz

mi_matriz = inicializar_matriz(2,4,1)



'''
1. Realizar una función que permita realizar la suma entre dos matrices, recibirá una matriz_a y una matriz_b y devuelve una matriz resultante con la suma de las mismas.
Tanto la matriz A como la matriz B deben tener la misma cantidad de filas y columnas, validar que eso ocurra (Podemos hacer otra función que se encargue de esto) , caso contrario retornar una lista vacía en caso de que no se cumpla.
'''

matrix_1 = [[3,8],
            [4,6]]
matrix_2 = [[4,0],
            [1,-9]]

def verifify_equal_values(matrix_one:list,matrix_two:list):
    equals = True
    for i in range(len(matrix_one)):
        if len(matrix_one[i]) != len(matrix_two[i]):
            equals = False
            break
    return equals

def add_values(array_1:list,array_2:list):
    for i in range(len(array_1)):
        row = []
        for j in range(len(array_1[i])):
            column = []
            value = array_1[i][j] + array_2[i][j]
            column.append(value)
            row.append(column)
    return sum
print(add_values(matrix_1,matrix_2))