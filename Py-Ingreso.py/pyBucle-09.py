

i = 0
a = 0
while i < 5:
    i += 1
    num = input("Ingrese un numero: ")
    num = int(num)
    a += num
promedio = a / 5
print("La suma es: {} y su promedio es de : {}".format(a, promedio))