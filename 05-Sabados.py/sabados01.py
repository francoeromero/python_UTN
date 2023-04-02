# 3) Copa pistón!!!
# Se deberá generar un programa para registrar las estadísticas de los 10 integrantes de una carrera de autos.
# Se pedirá el ingreso de:
# nombre
#  edad (mayor a 18)
# nacionalidad del piloto (argentino, inglés, francés, brasilero, estadounidense)
#  cantidad de carreras ganadas (no pueden ser números negativos)
#  número del vehículo (no puede ser un número negativo)
# se necesita saber:
# *Nacionalidad del piloto más joven.
# *Cantidad de vehículos con número par.
# *Nombre del piloto con menos victorias y el número de auto impar.
# *Cantidad de pilotos mayores de 25 años con número de vehículo impar.
# *Nombre del piloto más joven con más victorias.
# *Nacionalidad del piloto más veterano con menos victorias.
# *Promedio de edad de los pilotos que tiene un vehículo con número par.

lista_integrantes = list(range(1, 11))
for i in lista_integrantes:
    nombre = input("Ingrese su nombre: ")
    while(not nombre.isalpha()):
        nombre = input("Error! ingrese su nombre: ")
    edad_ingresada = input("Ingrese su edad: ")
    edad = int(edad_ingresada)
    while(edad < 17 or edad.isalpha()):
        edad_ingresada = input("ERROR! debes tener mas de 18 años: ")
        edad = int(edad_ingresada)
