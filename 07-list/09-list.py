# Crea una lista de números enteros y pide al usuario que ingrese otro número entero. Luego, busca el número ingresado en la lista y muestra la posición en la que se encuentra. Si el número no se encuentra en la lista, muestra un mensaje indicando que no se encontró

# numero = input("Ingrese un numero: ")
# numero = int(numero)
numeros = [1, 3, 2, 5, 8, 0, 2, 6]
i = 0
while(i < len(numeros)):
    if(i == 3):
        print("el numero es {} y su posicion es: {}".format(i, numeros.index(i)))
        break
    i += 1
    