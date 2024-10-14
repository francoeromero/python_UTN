'''
Ejercitación Clase 11 (Ordenamiento)

ARRAYS UNIDIMENSIONALES

'''


'''
1.Realizar una función que ordene una lista de enteros de forma ascendente (menor a mayor) , la misma debería devolver False en caso de que se ya se encuentre ordenada. True en caso contrario
'''

lista_ejemplo = [12,4,7,1,9]
lista_ordenada = [2,1,3,4,5]

def verificar_orden_ascendente(lista:list)->bool:
    ordenada = True
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                ordenada = False
                break
    return ordenada

def ordenar_ascendente(lista:list)->bool:
    verificacion = verificar_orden_ascendente(lista)
    if verificacion == False:
        for i in range(len(lista)):
            for j in range(i+1,len(lista)):
                if lista[i] > lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

    return verificacion 

'''
2.Realizar una función que ordene una lista de enteros de forma descendente (mayor a menor) , la misma debería devolver False en caso de que se ya se encuentre ordenada. True en caso contrario
'''

def verificar_orden_descendente(lista:list)->bool:
    ordenada = True
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] < lista[j]:
                ordenada = False
                break
    return ordenada

def ordenar_descendente(lista:list)->bool:
    verificacion = verificar_orden_descendente(lista)
    if verificacion == False:
        for i in range(len(lista)):
            for j in range(i+1,len(lista)):
                if lista[i] < lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

    return verificacion 


'''
3.Realizar una función que ordene una lista de enteros en orden ascendente o descendente dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad de intercambios que se realizaron.
'''

def ordenar(lista:list,ascendente:bool)->int:
    contador_modificaciones = 0
    if ascendente:
        for i in range(len(lista)):
            for j in range(i+1,len(lista)):
                if lista[i] > lista[j]:
                    contador_modificaciones+=1
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    else:
        for i in range(len(lista)):
            for j in range(i+1,len(lista)):
                if lista[i] < lista[j]:
                    contador_modificaciones+=1
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    return contador_modificaciones


'''
4.Realizar una función que ordene una lista de nombres de la alfabéticamente (A-Z) o viceversa (Z-A) dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad de cambios que se realizaron. 
Investigar cómo comparar str alfabéticamente en python.
'''
def ordenar_nombres(lista_nombres:list,ascendiente:bool)->int:
    modificaciones = 0
    if ascendiente:
        for i in range(len(lista_nombres)):
            for j in range(i+1,len(lista_nombres)):
                if lista_nombres[i] > lista_nombres[j]:
                    modificaciones += 1
                    aux = lista_nombres[i]
                    lista_nombres[i] = lista_nombres[j]
                    lista_nombres[j] = aux
    else:
        for i in range(len(lista_nombres)):
            for j in range(i+1,len(lista_nombres)):
                if lista_nombres[i] < lista_nombres[j]:
                    modificaciones += 1
                    aux = lista_nombres[i]
                    lista_nombres[i] = lista_nombres[j]
                    lista_nombres[j] = aux
    return modificaciones
'''
5. Similar a la función anterior, se debe realizar otra que ordene una lista de nombres por su largo, de manera ascendente o descendente, la función debe retornar la cantidad de cambios que se realizaron
'''

def ordenar_nombres_largo(lista_nombres:list,ascendiente:bool)->int:
    modificaciones = 0
    if ascendiente:
        for i in range(len(lista_nombres)):
            for j in range(i+1,len(lista_nombres)):
                if len(lista_nombres[i]) > len(lista_nombres[j]):
                    modificaciones += 1
                    aux = lista_nombres[i]
                    lista_nombres[i] = lista_nombres[j]
                    lista_nombres[j] = aux
    else:
        for i in range(len(lista_nombres)):
            for j in range(i+1,len(lista_nombres)):
                if len(lista_nombres[i]) < len(lista_nombres[j]):
                    modificaciones += 1
                    aux = lista_nombres[i]
                    lista_nombres[i] = lista_nombres[j]
                    lista_nombres[j] = aux
    return modificaciones
