# Crea una lista con 5 números enteros. Luego solicita un nuevo número y reemplaza el tercer elemento de la lista por el número ingresado. Finalmente imprime todos los números

lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista original: ", lista_numeros)
reemplazo_ingresado = input("Ingrese un nuevo numero: ")
reemplazo = int(reemplazo_ingresado)
lista_numeros[2] = reemplazo
print("Lista cambiada: ", lista_numeros)