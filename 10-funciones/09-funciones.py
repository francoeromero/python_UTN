# Crear una función que cuente la cantidad de veces que aparece un elemento en una lista. Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.

lista_elementos = [2, 3, 2, 5, 6]
elemento_elegido = 2

def contador(lista, elemento):
    contar = 0
    for i in lista:
        if(i == elemento):
            contar += 1
    return contar
print(contador(lista_elementos, elemento_elegido))


def cuanto(lista):
    contar = 0
    for i in lista:
        if lista.count(i) > 1:
            elemento_repetido = i
            contar += 1
    return elemento_repetido
print("El elemento repetido es {} y se repitio {} veces".format(cuanto(lista_elementos), contar))


"""
25 min______ 1 pomo
720 min______ x pomo 28

1 pomo ____ 25 min
20 pomo_____  500 min 8 horas

"""







# def contador(lista, elemento):
#     for i in lista:
#         if lista.count(i) > 1:
#             print("El elemento {} se repite")
# print(contador(lista_elementos, 2))
