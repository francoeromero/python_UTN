# Crea un diccionario que represente los gastos de una persona en diferentes categorías, donde las claves son los nombres de las categorías y los valores son los gastos correspondientes. Calcula el total de gastos de la persona.

gastos = {
    "comida" : 30000,
    "gimnasio" : 5000,
    "viaticos" : 4500,
    "comida de perros" : 5000
}
total_gastos = 0
for i in gastos:
    total_gastos += gastos[i]
print("Total gastos: ", total_gastos)