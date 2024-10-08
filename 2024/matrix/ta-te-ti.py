'''
TAREA:

Dada una matriz 3x3 (inicializada en todos ceros) Realizar un tateti en el que el jugador pueda jugar una partida contra la máquina, primero se le pedirá al jugador cara o cruz, si el jugador acierta comienza jugando sino comienza la máquina.
Cuando el usuario juega debe elegir en que posición de la matriz cargar su jugada , cuando el jugador elija se llenará con una “X” esa posición.
Cuando la máquina juegue elegirá una posición aleatoria de la matriz que no haya sido asignada y la llenará con una “O”.

'''
import random


def inicializar_matriz(cant_filas:int,cant_columnas:int, valor_inicial:any)->list:
    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz

def mostrar_tablero(matriz:list):
    string = '\n'
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            string += ' '
            string += matriz[fil][col]
        string += '\n'
    return string

# print(mostrar_tablero(mi_matriz))


def ingresar_opciones_numericas(mensaje:str,mensaje_error:str,lista_opciones:list):
    # validación
    dato = int(input(mensaje))
    while dato not in lista_opciones:
        dato = input(mensaje_error)
    return dato

def ingresar_opciones_string(mensaje:str,mensaje_error:str,lista_opciones:list):
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


def iniciador_juego()->str:
    cara_cruz_usuario = ingresar_opciones_numericas('Ingrese cara o cruz(1 = cara/ 2 = cruz): ', 'Ingrese correctamente (1 = cara/ 2 = cruz): ',[1,2] )
    numero_aleatorio = random.randint(1,2)

    if numero_aleatorio ==  cara_cruz_usuario:
        return 'usuario'
    else:
        return 'maquina'

def verificar_casilleros(matriz:list)->bool:
    casillero_vacio = False # esta lleno
    array = []
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            if matriz[fil][col] == '□':
                casillero_vacio = True # esta vacio
                break
    return casillero_vacio

def verificar_ganador(matriz:list,simbolo)->bool:
    ganador = False

    if simbolo == matriz[0][0] and simbolo == matriz[0][1] and simbolo == matriz[0][2]:
        return True
    elif simbolo == matriz[1][0] and simbolo == matriz[1][1] and simbolo == matriz[1][2]:
        return True
    elif simbolo == matriz[2][0] and simbolo == matriz[2][1] and simbolo == matriz[2][2]:
        return True
    elif simbolo == matriz[0][0] and simbolo == matriz[1][0] and simbolo == matriz[2][0]:
        return True
    elif simbolo == matriz[0][1] and simbolo == matriz[1][1] and simbolo == matriz[2][1]:
        return True
    elif simbolo == matriz[0][2] and simbolo == matriz[1][2] and simbolo == matriz[2][2]:
        return True
    # elif simbolo == matriz[0][0] and simbolo == matriz[1][1] and simbolo[2][2]:
    #     return True
    # elif simbolo == matriz[0][2] and simbolo == matriz[1][1] and simbolo[2][0]:
    #     return True
    
def ta_te_ti():
    # iniciamos la matriz
    tablero = inicializar_matriz(3,3,'□')
    # identificacion de simbolos usuario y maquina
    simbolo_usuario = ingresar_opciones_string('Ingresa que simbolo quieres usar (x/o)', 'solo puedes usar (x/o)',['x','o'])
    if simbolo_usuario == 'x':
        simbolo_maquina = 'o'
    else:
        simbolo_maquina = 'x'

    # quien empieza
    iniciador = iniciador_juego()
    if iniciador == 'usuario':

        while verificar_casilleros(tablero):
            fila_usuario = (ingresar_opciones_numericas('Selecciona la fila del tablero\n Primera fila: 1\n Segunda fila: 2\n Tercera fila: 3\n', 'Selecciona correctamente\n Primerafila: 1\n Segunda fila: 2\n Tercera fila: 3\n', [1,2,3])) - 1
            columna_usuario = (ingresar_opciones_numericas('Selecciona la columna del tablero\n Primera columna: 1\n Segunda columna: 2\n Tercera columna: 3\n','Seleccionacorrectamente\n Primera columna: 1\n Segunda columna: 2 Tercera columna: 3\n',[1,2,3]))-1

            while tablero[fila_usuario][columna_usuario] != '□':
                print('El casillero seleccionado ya esta ocupado, selecciona otro')
                fila_usuario = (ingresar_opciones_numericas('Selecciona la fila del tablero\n Primera fila: 1\n Segunda fila: 2\n Tercera fila: 3\n', 'Selecciona correctamente\nPrimera fila: 1\n Segunda fila: 2\n Tercera fila: 3\n', [1,2,3])) - 1
                columna_usuario = (ingresar_opciones_numericas('Selecciona la columna del tablero\n Primera columna: 1\n Segunda columna: 2\n Tercera columna: 3\n','Seleccionacorrectamente\n Primera columna: 1\n Segunda columna: 2 Tercera columna: 3\n',[1,2,3]))-1
            # selecciono la ubicacion que se reemplaze con el simbolo elegido
            tablero[fila_usuario][columna_usuario] = simbolo_usuario
            print(mostrar_tablero(tablero))

            if verificar_ganador(tablero,simbolo_usuario):
                print("FELICIDADES GANASTE !!! ")
                break

            # selecciona la maquina
            fila_maquina = random.randint(0,2)
            columna_maquina = random.randint(0,2)
                
            if tablero[fila_maquina][columna_maquina] != '□':
                fila_maquina = random.randint(0,2)
                columna_maquina = random.randint(0,2)
            tablero[fila_maquina][columna_maquina] = simbolo_maquina
            print(mostrar_tablero(tablero))
            
            if verificar_ganador(tablero,simbolo_maquina):
                print("PERDISTE")
                break
    else:
        while verificar_casilleros(tablero):
            # la maquina
            fila_maquina = random.randint(0,2)
            columna_maquina = random.randint(0,2)

            if tablero[fila_maquina][columna_maquina] != '□':
                fila_maquina = random.randint(0,2)
                columna_maquina = random.randint(0,2)
            tablero[fila_maquina][columna_maquina] = simbolo_maquina
            print(mostrar_tablero(tablero))

            if verificar_ganador(tablero,simbolo_usuario):
                print("FELICIDADES GANASTE !!! ")
                break

            # el usuario

            fila_usuario = (ingresar_opciones_numericas('Selecciona la fila del tablero\n Primera fila: 1\n Segunda fila: 2\n Tercera fila: 3\n', 'Selecciona correctamente\n Primerafila: 1\n Segunda fila: 2\n Tercera fila: 3\n', [1,2,3])) - 1
            columna_usuario = (ingresar_opciones_numericas('Selecciona la columna del tablero\n Primera columna: 1\n Segunda columna: 2\n Tercera columna: 3\n','Seleccionacorrectamente\n Primera columna: 1\n Segunda columna: 2 Tercera columna: 3\n',[1,2,3]))-1

            while tablero[fila_usuario][columna_usuario] != '□':
                print('El casillero seleccionado ya esta ocupado, selecciona otro')
                fila_usuario = (ingresar_opciones_numericas('Selecciona la fila del tablero\n Primera fila: 1\n Segunda fila: 2\n Tercera fila: 3\n', 'Selecciona correctamente\nPrimera fila: 1\n Segunda fila: 2\n Tercera fila: 3\n', [1,2,3])) - 1
                columna_usuario = (ingresar_opciones_numericas('Selecciona la columna del tablero\n Primera columna: 1\n Segunda columna: 2\n Tercera columna: 3\n','Seleccionacorrectamente\n Primera columna: 1\n Segunda columna: 2 Tercera columna: 3\n',[1,2,3]))-1
            # selecciono la ubicacion que se reemplaze con el simbolo elegido
            tablero[fila_usuario][columna_usuario] = simbolo_usuario
            print(mostrar_tablero(tablero))

            if verificar_ganador(tablero,simbolo_maquina):
                print("PERDISTE")
                break

        print('fin del juego')
            
ta_te_ti()



