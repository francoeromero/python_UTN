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

'''
5. Realizar una función que permita realizar la multiplicación entre dos matrices, recibirá una matriz_a y una matriz_b y devuelve una matriz resultante con el producto de las mismas.
Para que se pueda hacer una multiplicación entre dos matrices la cantidad de columnas de la matriz A debe ser igual a la cantidad de filas de la matriz B , si no se cumple devolver una lista vacía.
Además el tamaño de la matriz resultante debe ser equivalente a la cantidad de filas de la matriz A y la cantidad de columnas de la matriz B
'''

'''
la primera debe tener el mismo numero de columnas que filas de la segunda
'''
def verificar_multiplicacion_matrices(primera_matriz:list,segunda_matriz:list)->bool:
    
    # cuantas filas cada una
    cant_filas_matriz_a = len(primera_matriz)
    cant_filas_matriz_b = len(segunda_matriz)
    # cuantas col por cada fila
    columnas_a = []
    columnas_b = [] 
    for fil_a in range(cant_filas_matriz_a):
        cant_col_matriz_a = 0
        for col_a in range(len(primera_matriz[fil_a])):
            cant_col_matriz_a += 1
        columnas_a.append(cant_col_matriz_a)

    for fil_b in range(cant_filas_matriz_b):
        cant_col_matriz_b = 0
        for col_a in range(len(segunda_matriz[fil_b])):
            cant_col_matriz_b += 1
        columnas_b.append(cant_col_matriz_b)

    # verificar misma cantidad de columnas en cada fila
    misma_cantidad_columnas_a = True
    for i in range(len(columnas_a)):
        if columnas_a[0] != columnas_a[i]:
            misma_cantidad_columnas_a = False
            break

    misma_cantidad_columnas_b = True
    for j in range(len(columnas_b)):
        if columnas_b[0] != columnas_b[j]:
            misma_cantidad_columnas_b = False
            break
    
    if misma_cantidad_columnas_a == False or misma_cantidad_columnas_b == False:
        print('No se pueden multiplicar porque hay cantidad de columnas diferentes por cada fila')
        return False
    else:
        cantidad_columnas_a = columnas_a[0]
        cantidad_columnas_b = columnas_b[0]    
    
    # verificar la primera matriz debe ser igual de numero de columnas que de la fila de la segunda matriz
    if cantidad_columnas_a == cant_filas_matriz_b:
        print('Se pueden multiplicar las matrices')
        return True
    else:
        print('No se pueden multiplicar')
        return False

# a = [[5,3],
#     [-2,9],
#     [7,-4]]
# b = [[-2,8,5,3],
#     [5,-6,7,-7]]

def multiplicar_matrices(matriz_a:list,matriz_b)->list:
    matriz_multiplicada = []
    if verificar_multiplicacion_matrices(matriz_a,matriz_b):
        for fil in range(len(matriz_a)): # 3 VUELTAS (filas de la matriz a, reinicia la fila de multiplicacion)
            fila_multiplicada = []
            for col_b in range(len(matriz_b[0])): # 4 VUELTAS (columnas de la matriz b, reinicia la suma)
                suma = 0
                for equidad in range(len(matriz_a[fil])): # 2 VUELTAS (se suman los resultados)
                    suma = suma + (matriz_a[fil][equidad] * matriz_b[equidad][col_b])
                fila_multiplicada.append(suma)
            matriz_multiplicada.append(fila_multiplicada)
        
        return matriz_multiplicada
    else:
        return matriz_multiplicada

# print(multiplicar_matrices(a,b))






        # matriz_a[0][0] * matriz_b[0][0]
        # matriz_a[0][1] * matriz_b[1][0]
        
        # matriz_a[0][0] * matriz_b[0][1]
        # matriz_a[0][1] * matriz_b[1][1]
        
        # matriz_a[0][0] * matriz_b[0][2]
        # matriz_a[0][1] * matriz_b[1][2]

        # matriz_a[0][0] * matriz_b[0][3]
        # matriz_a[0][1] * matriz_b[1][3]



        # matriz_a[1][0] * matriz_b[0][0]
        # matriz_a[1][1] * matriz_b[1][0]
        
        # matriz_a[1][0] * matriz_b[0][1]
        # matriz_a[1][1] * matriz_b[1][1]
        
        # matriz_a[1][0] * matriz_b[0][2]
        # matriz_a[1][1] * matriz_b[1][2]

        # matriz_a[1][0] * matriz_b[0][3]
        # matriz_a[1][1] * matriz_b[1][3]
        


        # matriz_a[2][0] * matriz_b[0][0]
        # matriz_a[2][1] * matriz_b[1][0]
        
        # matriz_a[2][0] * matriz_b[0][1]
        # matriz_a[2][1] * matriz_b[1][1]
        
        # matriz_a[2][0] * matriz_b[0][2]
        # matriz_a[2][1] * matriz_b[1][2]

        # matriz_a[2][0] * matriz_b[0][3]
        # matriz_a[2][1] * matriz_b[1][3]