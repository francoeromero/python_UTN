# Dado un número entero n, imprimir la secuencia de números de Harshad menores o iguales a n.
numero = 21
numero_str = str(numero)
cantidad_digitos = len(numero_str)
primer_digito = int(numero_str[0])
segundo_digito = int(numero_str[1])
suma = 0
for i in range(cantidad_digitos):
    suma = primer_digito + segundo_digito
print(suma)

# n_ingresado = input("Ingrese un numero: ")
# n = int(n_ingresado)
for i in range(10, 11):
    for numero in range(len(str(i))):
        print() # quiero imprimir el primer digito del numero 

# for i in range(10, 11):
#     print(i)