def inicializar_matriz(cant_filas:int,cant_columnas:int, valor_inicial:any)->list:
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

# matriz_1 = [[3,8],
#             [4,6]]
# matriz_2 = [[4,0],
#             [1,-9]]

# matriz_1 = inicializar_matriz(2,2,4)
# matriz_2 = inicializar_matriz(2,2,3)

def verificar_igualdad(matriz_a:list,matriz_b:list)->bool:
    igualdad = True
    if len(matriz_a) != len(matriz_b):
        igualdad = False
    return igualdad
# print(verificar_igualdad(matriz_1,matriz_2))

def suma_matrices(matriz_a:list,matriz_b:list)->list:
    if verificar_igualdad(matriz_a, matriz_b):
        nueva_matriz = []
        for fil in range(len(matriz_a)):
            fila = []
            for col in range(len(matriz_a[fil])):
                suma = matriz_a[fil][col] + matriz_b[fil][col]
                fila.append(suma)
            nueva_matriz.append(fila)
        return nueva_matriz
    else:
        return 'No hay igualdad en la cantidad de filas de las dos matrices'

# print(suma_matrices(matriz_1,matriz_2))


'''
2. Realizar una función que permita realizar el producto (multiplicación) de una matriz por un escalar (número entero) , la función deberá recibir la matriz a la que se le quiera realizar el producto, el número entero que multiplique a está matriz, la función devuelve una matriz nueva con el resultado de la multiplicación.
'''

matriz_1 = [[3,8],
             [4,6]]

def producto_matriz(matriz_1:list,num_producto:int)->list:
    nueva_matriz = []
    for fil in range(len(matriz_1)):
        fila = []
        for col in range(len(matriz_1[fil])):
            producto = matriz_1[fil][col] * num_producto
            fila.append(producto)
        nueva_matriz.append(fila)
    return nueva_matriz

# print(producto_matriz(matriz_1,2))

'''
3. Realizar una función que reciba una matriz , calcule y retorne en una nueva lista su matriz opuesta
'''
def matriz_opuesta(matriz_a:list)->list:
    matriz_opuesta = []
    for fil in range(len(matriz_a)):
        fila = []
        for col in range(len(matriz_a[fil])):
            opuesto = matriz_a[fil][col] * - 1
            fila.append(opuesto)
        matriz_opuesta.append(fila)
    return matriz_opuesta

# matrizz = [[3,8],
#              [4,6]]
# print(matriz_opuesta(matrizz))


'''
4. Realizar una función que reciba una matriz , calcule y retorne en una nueva lista su matriz traspuesta (Donde las columnas y las filas se intercambian)
'''

def matriz_traspuesta(matriz_ingresada:list)->list:
    matriz_traspuesta = []
    for col in range(len(matriz_ingresada[0])): # 3 vueltas
        nueva_columna = []
        for fil in range(len(matriz_ingresada)): # 2 vueltas
            nueva_columna.append(matriz_ingresada[fil][col])
        matriz_traspuesta.append(nueva_columna)
    return matriz_traspuesta
    
# mi_matriz = [[3,8,5],
#              [4,6,3]]

# print(matriz_traspuesta(mi_matriz))
