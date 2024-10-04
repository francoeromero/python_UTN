def verificar_existencia(variable,mensaje_negativo):
    existe = True
    if variable == None:
        print(mensaje_negativo)
        existe = False
    return existe

def ingresar_string(mensaje:str,mensaje_error:str,min:int)->str:
    string = input(mensaje)
    while len(string) < min:
        string = input(mensaje_error)
    return string

def ingresar_digitos(mensaje:str,mensaje_error:str,min:int,max:int)->int:
    digitos = input(mensaje)
    while len(digitos) < min or len(digitos) > max:
        digitos = input(mensaje_error)
    digitos = int(digitos)
    return digitos

def ingresar_opciones(mensaje:str,mensaje_error:str,lista_opciones:list):
    # pasar a minuscula
    lista_a_minuscula = []
    for i in range(len(lista_opciones)):
        lower = lista_opciones[i].lower()
        lista_a_minuscula.append(lower)
    # validación
    dato = input(mensaje)
    while dato not in lista_a_minuscula:
        dato = input(mensaje_error)
    return dato

def ingresar_numero_entero(mensaje:str,mensaje_error:str,min:int,max):
    numero = int(input(mensaje))
    while numero < min or numero > max:
        numero = int(input(mensaje_error))
    return numero
    
def promedio(cantidad:int,acumulador:int)->int:
    if cantidad > 0:
        promedio = acumulador / cantidad 
    else:
        promedio = 0
    return promedio

def porcentajes(lista_nombres:list,lista_valores:list):
    total = sum(lista_valores)
    porcentajes = []
    mensaje = ''
    if len(lista_nombres) == len(lista_valores):
        for i in range(len(lista_valores)):
            resultado = (lista_valores[i] * 100) / total
            porcentajes.append(resultado)
            mensaje += f'{lista_nombres[i]}: {resultado} % '
        return mensaje
    else:
        return 'las listas tienen que ser equitativas'

'''
1.
'''
def registrar_alumnos(cantidad_alumnos:int,):
    matriz = []
    for fil in range(cantidad_alumnos):
        fila = []
        # columna 0
        nombre = ingresar_string('ingrese un nombre: ','ingrese correctamente el nombre', 3)
        # columna 1
        apellido = ingresar_string('ingrese un apellido: ','ingrese correctamente el apellido', 3)
        # columna 2
        dni = ingresar_digitos('ingrese dni: ', 'ingrese correctamente el dni(6 a 8 caracteres): ', 6, 8)
        # columna 3
        genero = ingresar_opciones('ingrese el genero(M para masculino, F para femenino, NB para No Binario): ', 'ingrese correctamente(M para masculino, F para femenino, NB para No Binario): ', ['M','F','NB'])
        # columna 4
        nota_final = ingresar_numero_entero('ingrese la nota final(Número entre 1 y 10): ', 'ingrese correctamente la nota(Número entre 1 y 10): ', 1,10)
        # metemos todas las columnas en una fila
        fila.append(nombre)
        fila.append(apellido)
        fila.append(dni)
        fila.append(genero)
        fila.append(nota_final)
        # la fila se mete ala matriz
        matriz.append(fila)
    return matriz
'''
2.
'''
def mostrar_mensaje_alumnos_registrados(matriz:list):
    mensaje = '\n|| nombre || apellido || dni || genero || nota final ||\n'
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            if col == 4:
                mensaje += f'|| {matriz[fil][col]} ||\n'
            else:
                mensaje += f'|| {matriz[fil][col]}'
    return mensaje 
'''
3, 4 ,5
'''    
def filtrar_notas(matriz:list, nota_minima:int, nota_maxima, mensaje_negativo:str):
    cantidad_filtrados = 0
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            if matriz[fil][4] >= nota_minima and matriz[fil][4] <= nota_maxima:
                cantidad_filtrados += 1
    if cantidad_filtrados > 0:
        return cantidad_filtrados
    else:
        return mensaje_negativo
    
'''
6.
'''    
def verificar_alumno_dni(matriz:list):
    dni = int(input('ingrese dni del alumno: '))
    encontrado = False
    mensaje = 'No se encontró en el sistema'
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            if matriz[fil][2] == dni:
                encontrado = True
                break
    if encontrado == True:
        mensaje = 'Se encontró en el sistema'
    return mensaje
'''
8.
'''
def promedio_alumnos(matriz:list):
    cantidad_alumnos = len(matriz)
    acumulador_notas = 0
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            if col == 4:
                acumulador_notas += matriz[fil][col] 
    promedio_total = promedio(cantidad_alumnos,acumulador_notas)
    return promedio_total
'''
9.
'''
def promedio_alumnos_masculinos(matriz:list):
    masculinos = 0
    acumulador_notas = 0
    for fil in range(len(matriz)):
        if matriz[fil][3] == 'm':
            acumulador_notas += matriz[fil][4]
            masculinos += 1
    promedio_masculinos = promedio(masculinos,acumulador_notas)
    return promedio_masculinos
                                
'''
10.
'''
def porcentaje_alumnos(matriz:list):
    fem = 0
    masc = 0
    nob = 0
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            if col == 3:
                if matriz[fil][col] == 'f':
                    fem += 1
                elif matriz[fil][col] == 'm':
                    masc += 1
                else:
                    nob += 1
    lista_cantidad_generos = [fem,masc,nob]
    lista_generos = ['femeninos', 'masculinos', 'no binarios']
    mensaje = porcentajes(lista_generos, lista_cantidad_generos)
    return mensaje

'''
11. alumno o alumnos con mayor nota 
'''
def mayor_nota(matriz:list)->list:
    matriz_maximos = []
    maximo = matriz[0][4]
    # primero encontrar la maxima nota de la matriz
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            if matriz[fil][4] > maximo:
                maximo = matriz[fil][4]

    # luego ver todas las repetidas segun la max nota
    for fil in range(len(matriz)):
        if matriz[fil][4] == maximo:
            matriz_maximos.append(matriz[fil])
    return matriz_maximos
'''
12. 
'''
def alumnos_mayor_nota_promedio(matriz:list)->list:
    nota_promedio = promedio_alumnos(matriz)
    nueva_matriz = []
    for fil in range(len(matriz)):
        if matriz[fil][4] > nota_promedio:
            nueva_matriz.append(matriz[fil])
    return nueva_matriz

                