# Crea un diccionario que contenga el nombre y el sueldo de varios empleados. Luego, permite al usuario aumentar el sueldo de un empleado y actualizar el valor correspondiente en el diccionario.

sueldos = {
    "pedro": 90000,
    "jorge" : 120000,
    "totito" : 20000,
    "javier" : 10000
}
nombre = input("Ingrese el nombre del empleado: ")
nuevo_sueldo = input("Ingrese nuevo sueldo: ")
nuevo_sueldo = int(nuevo_sueldo)
for i in sueldos:
    if(i == nombre):
        sueldos[i] = nuevo_sueldo
        print(sueldos)
        break