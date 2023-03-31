# Dado un número entero n, imprimir todos los números desde 1 hasta n en orden ascendente.
# pido un numero 
numero_ingresado = input("Ingrese un numero: ")
# lo paso a entero
numero_entero = int(numero_ingresado)
# numero inicial
numero = 1
# iteracion hasta que numero entero sea mayor al inicial
while(numero_entero >= numero):
    print(numero)
    numero = numero + 1


