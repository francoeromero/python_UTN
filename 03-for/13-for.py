# Dada una lista de palabras, imprimir las palabras que tienen una longitud impar.

palabras = []

for i in range(4):
    palabra = input("Ingrese una palabra: ")
    if(len(palabra) % 2 != 0):
        palabras.append(palabra)
print(palabras)