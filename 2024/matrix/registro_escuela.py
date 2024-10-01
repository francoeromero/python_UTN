'''
Ejercitación Clase 10 (Listas Anidadas)

Debemos realizar un programa que nos permita inscribir 10 alumnos en el sysacad.
Debemos guardar la información de estos alumnos en una matriz de 10 filas y 5 columnas.
Cada fila va a guardar la información individual de cada alumno.
Cada columna guarda un dato diferente del alumno siguiendo el siguiente orden (Nombre,Apellido,DNI,Género,Nota Final)

El sistema debe pedir:

Nombre (Validar que se ingresó un str de al menos 3 caracteres)
Apellido (Validar que se ingresó un str de al menos 3 caracteres)
DNI (Número entre 6 y 8 caracteres) 
Género (M para masculino, F para femenino, NB para No Binario)
Nota Final (Número entre 1 y 10)

El sistema debe tener un menú como el siguiente (Pueden usar de base menu.py de la Calculadura por ejemplo)

Debemos cargar todo de manera algorítmica sin usar append inicializando anteriormente la matriz de alumnos con la función vista la clase anterior.

1.Ingresar 10 alumnos:Realiza lo explicado anteriormente
2.Mostrar Todos los Alumnos:Mostrar la información de cada alumno en un formato que quede lindo para el usuario
3.Mostrar Alumnos Promocionados:Mostrar sólo la información de los alumnos con nota mayor a 6 , en caso de no haber informar que no hay
4.Mostrar Alumnos Aprobados:Mostrar sólo la información de los alumnos con nota 4,5 , en caso de no haber informar que no hay
5.Mostrar Alumnos Desaprobados:Mostrar sólo la información de los alumnos con nota menor a 4 , en caso de no haber informar que no hay.
6.Buscar Alumno por DNI:Se debe ingresar el DNI de un alumno y buscar si se encuentra o no en el sistema, mostrar su información también.
7.La cantidad de alumnos promocionados, aprobados y desaprobados
8.El promedio de nota de todos los alumnos
9.El promedio de nota de los alumnos masculinos
10.El porcentaje de alumnos de cada género
11.Mostrar el alumno o los alumnos con mayor nota
12.Mostrar la cantidad de alumnos que superan la nota promedio
13.Salir

NOTA 1: No se puede acceder de la opción 2 a la 12 si nunca se ingresó la opción 1.
NOTA 2: Modularizar cada tarea en funciones, recordar hacerlas lo más genéricas posibles.

'''

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



# nombre = ingresar_string('ingrese un nombre: ','ingrese correctamente el nombre', 3)
# apellido = ingresar_string('ingrese un apellido: ','ingrese correctamente el apellido', 3)
# dni = ingresar_digitos('ingrese dni: ', 'ingrese correctamente el dni(6 a 8 caracteres): ', 6, 8)
# genero = ingresar_opciones('ingrese el genero(M para masculino, F para femenino, NB para No Binario): ', 'ingrese correctamente(M para masculino, F para femenino, NB para No Binario): ', ['M','F','NB'])
# nota_final = ingresar_numero_entero('ingrese la nota final(Número entre 1 y 10): ', 'ingrese correctamente la nota(Número entre 1 y 10): ', 1,10)
# funciones = [nombre,apellido,dni,genero,nota_final]

# def crea_matriz(cantidad_filas:int,lista_funciones:list):
#     matriz = []
#     for fil in range(cantidad_filas):
#         fila = []
#         for col in range(len(lista_funciones)):
#             columna = lista_funciones[col]
#             fila.append(columna)
#         matriz.append(fila)
#     return matriz

# print(crea_matriz(3,funciones))




def crear_matriz(cantidad_alumnos:int,):
    matriz = []
    for fil in range(cantidad_alumnos):
        fila = []
        # columna 1
        nombre = ingresar_string('ingrese un nombre: ','ingrese correctamente el nombre', 3)
        # columna 2
        apellido = ingresar_string('ingrese un apellido: ','ingrese correctamente el apellido', 3)
        # columna 3
        dni = ingresar_digitos('ingrese dni: ', 'ingrese correctamente el dni(6 a 8 caracteres): ', 6, 8)
        # columna 4
        genero = ingresar_opciones('ingrese el genero(M para masculino, F para femenino, NB para No Binario): ', 'ingrese correctamente(M para masculino, F para femenino, NB para No Binario): ', ['M','F','NB'])
        # columna 5
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
# print(mostrar_matriz(2))

def mostrar_mensaje_alumnos_registrados(matriz:list):
    mensaje = '\n|| nombre || apellido || dni || genero || nota final ||\n'
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            if col == 4:
                mensaje += f'|| {matriz[fil][col]} ||\n'
            else:
                mensaje += f'|| {matriz[fil][col]}'
    return mensaje 

alumnos = crear_matriz(2)
# print(mostrar_mensaje_alumnos_registrados(alumnos))

'''
3.Mostrar Alumnos Promocionados:Mostrar sólo la información de los alumnos con nota mayor a 6 , en caso de no haber informar que no hay
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
    
alumnos_promocionados = filtrar_notas(alumnos,6,10,'no existen alumnos promocionados')


'''
4.Mostrar Alumnos Aprobados:Mostrar sólo la información de los alumnos con nota 4,5 , en caso de no haber informar que no hay
'''

alumnos_aprobados = filtrar_notas(alumnos,4,5,'no existen alumnos aprobados')

'''
5.Mostrar Alumnos Desaprobados:Mostrar sólo la información de los alumnos con nota menor a 4 , en caso de no haber informar que no hay.
'''
alumnos_desaprobados = filtrar_notas(alumnos,1,4,'no existen alumnos desaprobados')

'''
6.Buscar Alumno por DNI:Se debe ingresar el DNI de un alumno y buscar si se encuentra o no en el sistema, mostrar su información también.
'''
def verificar_alumno_dni(matriz:list):
    dni = input('ingrese dni del alumno: ')
    encontrado = False
    mensaje = 'No se encontró en el sistema'
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            if col == 2:
                if matriz[fil][col] == dni:
                    encontrado = True
                    break
    if encontrado == True:
        mensaje = 'Se encontró en el sistema'
    return mensaje

'''
7.La cantidad de alumnos promocionados, aprobados y desaprobados
'''