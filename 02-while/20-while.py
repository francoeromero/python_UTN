# Dado un número entero n, imprimir todos los números perfectos menores o iguales a n. Los números perfectos son aquellos números enteros positivos que son iguales a la suma de sus divisores propios (excluyendo al propio 

n_ingresado = input("Ingresar un numero: ")
n = int(n_ingresado)
i = 1 
while(i < n):
    if(n % i == 0):
        print(i)
    i += 1


# chat gpt

# # Definir una función para comprobar si un número es perfecto
# def es_numero_perfecto(numero):
#     suma = 0
#     i = 1
#     while i < numero:
#         if numero % i == 0:
#             suma += i
#         i += 1
#     return suma == numero

# # Crear una lista de números perfectos hasta un límite dado
# def numeros_perfectos_limite(limite):
#     numeros_perfectos = []
#     i = 1
#     while i <= limite:
#         if es_numero_perfecto(i):
#             numeros_perfectos.append(i)
#         i += 1
#     return numeros_perfectos

# # Ejemplo de uso
# print(numeros_perfectos_limite(10000))  # encuentra todos los números perfectos hasta el límite de 10000
