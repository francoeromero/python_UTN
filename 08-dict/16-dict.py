# Crea un diccionario que represente una lista de tareas pendientes, donde las claves son las tareas y los valores son "True" si están completadas y "False" si no lo están. Solicita al usuario el nombre de una tarea y modifica el valor para marcarla como completada. Imprimir el listado de tareas pendientes

lista_pendientes = {
    "correr en la plaza " : False,
    "ir al gimnasio" : True,
    "sacar a los perros" : True,
    "cenar" : True,
    "estudiar ingles" : False
}

tarea_solicitada = input("Ingrese la tarea: ")
completada = True
for i in lista_pendientes:
    if(tarea_solicitada == i):
        lista_pendientes[i] = completada
print(lista_pendientes)