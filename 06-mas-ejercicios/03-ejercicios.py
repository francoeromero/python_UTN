# Ingresar 5 números enteros, distintos de cero.
# Informar:
# a. Cantidad de pares e impares.
# b. El menor número ingresado.
# c. De los pares el mayor número ingresado.
# d. Suma de los positivos.
# e. Producto de los negativos.
i = 0
contador_pares = 0
contador_impares = 0
acumulador_positivos = 0
acumulador_negativos = 1
flag_maximo_par = 0
while(i < 5):
    numero_ingresado = input("Ingrese un numero entero: ")
    numero = int(numero_ingresado)
    if(numero % 2 == 0):
        contador_pares += 1
        if(flag_maximo_par == 0 or numero > max_par):
            max_par = numero
            flag_maximo_par = 1
    if(numero % 2 != 0):
        contador_impares += 1
    if(i == 0 or numero > max):
        max = numero
    if(numero > -1):
        acumulador_positivos += numero
    i += 1
    if(numero < 0):
        acumulador_negativos = acumulador_negativos * numero
print("Contador pares: {} Contador impares: {} Numero maximo: {} Numero maximo par: {} Suma de los positivos: {} Producto de los negativos: {}".format(contador_pares, contador_impares, max, max_par, acumulador_positivos, acumulador_negativos))
