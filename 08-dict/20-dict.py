# Crea un diccionario que represente los asientos de un avión, donde las claves son los números de asientos y los valores son "True" si están ocupados y "False" si no lo están. Solicita al usuario un número de asiento y modifica su valor para marcarlo como ocupado. Luego imprimí la lista de asientos libres

asientos_avion = {
    "asiento 1" : True,
    "asiento 2" : False,
    "asiento 3" : False,
    "asiento 4" : True,
    "asiento 5" : False,
    "asiento 6" : True,
    "asiento 7" : False,
    "asiento 8" : True,
}

asiento = input("Ingrese numero de asiento: ")

for i in asientos_avion:
    if asiento == i:
        asientos_avion[i] = True
print(asientos_avion)