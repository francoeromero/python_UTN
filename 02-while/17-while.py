# Dada una cadena de texto, imprimir la cadena al revés.

# cadena_texto = input("Ingrese una palabra para imprirla al reves: ")
# i = len(cadena_texto) - 1
# while(i >= 0):
#     print(cadena_texto[i])
#     i -= 1

cadena = input("Ingrese una palabra: ")
i = len(cadena) - 1
cadena_inversa = ""
while(i >= 0):
    cadena_inversa += cadena[i]
    i -= 1
print("la palabra al reves es: ", cadena_inversa)

# segun chat gpt

# cadena_texto = input("Ingrese una palabra: ")
# cadena_invertida = cadena_texto[::-1]
# print(cadena_invertida)
