# Dada una cadena de texto, imprimir cada uno de los caracteres en la cadena.

# cadena = "hola"
# print(len(cadena))

cadena = input("Ingrese una cadena de texto: ")
numero_inicial = 0
while (numero_inicial < len(cadena)):
    numero_inicial = numero_inicial + 1
    print(numero_inicial)

# cadena = input("Ingrese una cadena de texto: ")
# primer_letra = cadena[0]
# print(primer_letra)

# cadena = input("Ingrese su nombre: ")
# contador = 0
# while (len(cadena) > contador): # len() es la cantidad de letras ejemplo hola entonces es 4
#     print(cadena[contador]) # cadena[contador] lo que va entre corchetes representa el orden de cada letra 
#     contador = contador + 1 # sumamos 1 para que cada vuelta se vaya imprimiendo cada letra de la palabra

##########################################################
# la cantidad de elementos de una lista #
numeros = [1, 2, 4, 6]
cantidad_de_elementos_lista = len(numeros)
print(cantidad_de_elementos_lista)

# elegir un elemento de la lista #
numeros = [9, 3, 5]
elijo_el_primer_elemento_de_la_lista = numeros[0]
print(elijo_el_primer_elemento_de_la_lista)

# lo mismo pasa con las cadenas o string #
cadena = "hola"
cantidad_de_letras = len(cadena)
primera_letra = cadena[0]
print("la cantidad de letras es: {0} y la primera letra es: {1}".format(cantidad_de_letras, primera_letra))

