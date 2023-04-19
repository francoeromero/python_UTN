# num = None
# total = 0
# for i in range(5):
#     num = input("Ingrese un numero: ")
#     num = int(num)
#     total += num
# print("La suma de los numeros es {}".format(total))

# lista = []

# for i in range(5):
#     num = input("Ingrese un numero: ")
#     num = int(num)
#     lista.append(num)
# print("La lista de numeros seleccionados son: {}".format(lista))

# # for i in range(len(lista)):
# #     print(lista[i])
# acumulador=0
# for a in lista:
#     acumulador += a
# print("La suma de todos es {}".format(acumulador))


# buscar un numero
listaa = [1, 32, 22, 12]
numero_buscado = input("ingrese unnumero a buscar: ")
numero_buscado = int(numero_buscado)
# indice = 1

for i in range(len(listaa)):
    if(listaa[i] == numero_buscado):
        indice = i
        break
if(indice != -1):
    print("El numero esta en el indice {}".format(indice+1))
else:
    print("El numero no esta en la lista")
