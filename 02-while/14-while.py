# Dada una cadena de texto, imprimir la cantidad de veces que aparece una letra específica en la cadena.

cadena_texto = input("Ingrese una palabra: ")
letra_especifica = "n"
i = 0
while(len(cadena_texto) > i):
    if(cadena_texto[i] == letra_especifica):
        print(cadena_texto[i])
    i += 1
