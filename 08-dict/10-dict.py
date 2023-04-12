# Crea un diccionario que represente las notas de un examen de varios estudiantes, donde las claves son los nombres de los estudiantes y los valores son sus notas. Imprime el promedio de las notas.z

notas = {
    "Juancito" : 8,
    "Jose" : 3,
    "Gabriel" : 6
}
suma = 0
for i in notas:
    suma += notas[i]
promedio = suma / len(notas)
print(promedio)
    