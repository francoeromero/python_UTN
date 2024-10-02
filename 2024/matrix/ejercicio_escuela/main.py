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
s
NOTA 1: No se puede acceder de la opción 2 a la 12 si nunca se ingresó la opción 1.
NOTA 2: Modularizar cada tarea en funciones, recordar hacerlas lo más genéricas posibles.

'''
from funciones_gral import *

matriz_alumnos = None
alumnos_promocionados = None
alumnos_aprobados = None
alumnos_desaprobados = None
alumno_dni = None
alumnos_notas = None
promedio_total = None
promedio_nota_masculinos = None
porcentajes_generos = None
while True:
    print('\n REGISTRO DE ALUMNOS UTN ')
    print('1. Registrar alumnos')
    print('2. Mostrar alumnos registrados')
    print('3. Calcular estadisticas de los alumnos y Mostrar')
    print('4. Buscar alumno por DNI')
    print('5. Salir')
    # print('\n REGISTRO DE ALUMNOS UTN \n1. Registrar alumnos\n2. Mostrar alumnos registrados\n3. Cantidad de alumnos promocionados\n4. Cantidad de alumnos aprobados\n5. Cantidad de alumnos desaprobados\n6. Buscar alumno por DNI\n7. Cantidad de alumnos promocionados, aprobados y desaprobados\n.8 El promedio de nota de todos los alumnos\n.9 El promedio de nota de todos los alumnos masculinos\n.10. El porcentaje de alumnos de cada genero\n11. Mostrar el alumno o alumnos con mayor nota\n12. Mostrar la cantidad de alumnos que superan la nota promedio\n13.Salir')
    opcion = int(input('Ingrese una opcion: '))
    # while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 13:
    #     opcion = input('Ingrese correctamente, del 1 al 13: ')
    # opcion = int(opcion)
    match opcion :
        case 1:
            cantidad = 2
            matriz_alumnos = registrar_alumnos(cantidad)
        case 2:
            if verificar_existencia(matriz_alumnos,'\n\n No hay registro de alumnos'):
                mensaje_registro_alumnos = mostrar_mensaje_alumnos_registrados(matriz_alumnos)
                print(mensaje_registro_alumnos)
        case 3:
            if verificar_existencia(matriz_alumnos,'\n\n No hay registro de alumnos'):
                # Calculo
                alumnos_promocionados = filtrar_notas(matriz_alumnos,6,10,'no existen alumnos promocionados')
                alumnos_aprobados = filtrar_notas(matriz_alumnos,4,5,'no existen alumnos aprobados')
                alumnos_desaprobados = filtrar_notas(matriz_alumnos,1,4,'no existen alumnos desaprobados')
                alumnos_notas = [alumnos_promocionados,alumnos_aprobados,alumnos_desaprobados]
                promedio_total = promedio_alumnos(matriz_alumnos)
                promedio_nota_masculinos = promedio_alumnos_masculinos(matriz_alumnos)
                porcentajes_generos = porcentaje_alumnos(matriz_alumnos)
                mayores_notas = mayor_nota(matriz_alumnos)
                mayores_nota_promedio = alumnos_mayor_nota_promedio(matriz_alumnos)
                # Mostrar
                print(f'3. promocionados: {alumnos_promocionados}')
                print(f'4. aprobados: {alumnos_aprobados}')
                print(f'5. desaprobados: {alumnos_desaprobados}')
                print(f'7. cantidad promocionados, aprobados y desaprobados: {alumnos_notas}')
                print(f'8. promedio de nota de todos los alumnos: {promedio_total}')
                print(f'9. promedio de nota de los alumnos masculinos: {promedio_nota_masculinos}')
                print(f'10. porcentaje de alumnos de cada genero: {porcentajes_generos}')
                print(f'11. Alumnos con mayor nota: {mayores_notas}')
                print(f'12. Alumnos que superaron la nota promedio: {mayores_nota_promedio}')
                
        case 4:
            alumno_dni = verificar_alumno_dni(matriz_alumnos)
            print(f'6. alumno por dni: {alumno_dni}')
        case 5:
            print('saliendo del sistema')
            break





