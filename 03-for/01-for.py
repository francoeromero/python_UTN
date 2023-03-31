# Dada una lista de números, imprimir el número más grande de la lista.

def lista_mas_grande():
    # creo una variable y asigno una lista de numeros
    lista = [0, 2, 4, 6, 8, 10, 12, 20]
    # creo otra variable y le asigno el primer elemento de la lista
    maximo = lista[0]
    # for
    for numero in lista:
        if numero > maximo:
            maximo = numero
    print("El numero más grande en la lista es: ", maximo)
lista_mas_grande()

def lista_mas_chica():
    lista = [23, 5, 62, 3, 7]
    minimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
    print("El numero más chico es ", minimo)
lista_mas_chica()