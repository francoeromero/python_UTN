# Dada una lista de palabras, imprimir la cantidad total de vocales en la lista.

animales = ["perro", "gato", "pez", "lobo", "tigre"]
acumulador_letras = 0
for i in animales:
    acumulador_letras += len(i)
print("La cantidad de letras en la lista es: ", acumulador_letras)