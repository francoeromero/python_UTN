# Dado un número entero n, imprimir todos los números impares menores o iguales a n.
n_ingresado = input("Ingrese un numero: ")
n = int(n_ingresado)

# #con numeros pares
# while(n >= 0):
#     print(n)
#     n = n - 2

# #con numeros impares
# while(1 <= n):
#     if(n % 2 != 0):
#         print(n)
#         n = n - 2 # funciona solo si ingrese un numero impar

i = 0
while(i <= n):
    if(i % 2 != 0):
        print(i)
    i += 1