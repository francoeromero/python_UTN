# Crea un diccionario que represente las temperaturas de una ciudad durante una semana, donde las claves son los días de la semana y los valores son las temperaturas correspondientes. Calcula la temperatura promedio de la semana.

temperaturas = {
    "dia 1" : 39,
    "dia 2" : 35,
    "dia 3" : 32,
    "dia 4" : 43,
    "dia 5" : 35,
    "dia 6" : 39,
    "dia 7" : 31
}
suma = 0
for i in temperaturas:
    suma += temperaturas[i]
promedio = suma / len(temperaturas)
print("La suma es de {} y su promedio es de {}".format(suma, promedio))