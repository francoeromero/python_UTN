# Crea un diccionario que represente las edades de varias personas, donde las claves son los nombres de las personas y los valores son sus edades. Imprime la edad de la persona más joven.

# edades = [
#     {"Pablo":24},
#     {"Marcelo": 20},
#     {"Gabriel": 30}
# ]

edades = {
    "Pablo" : 24,
    "Juancito": 20,
    "Jose" : 30
}
# PARA IMPRIMIR LA CLAVE
# for i in edades:
#     print(i) # "Pablo", "Juancito", "Jose"

# PARA IMPRIMIR EL VALOR 
# for i in edades:
#     print(edades[i]) # 24, 20, 30


bandera = 0
minima_edad = 0
for i in edades:
    if(edades[i] < minima_edad or bandera == 0):
        minima_edad = edades[i]
        nombre_mas_joven = i
        bandera = 1
print(nombre_mas_joven,minima_edad)