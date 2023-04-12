# Crea un diccionario que contenga las capitales de los países de América del Sur. Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.

capitales = {
    "argentina": "Buenos Aires",
    "colombia" : "Quito",
    "bolivia" : "La paz",
    "peru" : "Lima"
}
# i representa cada pais
# capitales[i] representa la capital de cada uno

pais = input("Ingrese un pais: ")
for i in capitales:
    if(pais == i):
        print(capitales[i])

