# Ejercicio 4:
# Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
# distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
# ser soltero.'

edad_ingresada = input("Ingrese edad: ")
edad = int(edad_ingresada)
while(edad < 0):
    edad_ingresada = input("ERROR! ingrese edad correcta: ")
    edad = int(edad_ingresada)
estado_civil = input("Ingrese estado civil: ")
while(estado_civil != "casado" or estado_civil != "divorciado"):
    estado_civil = input("ERROR! ingrese estado civil correcto: ")

    if(edad < 17 and estado_civil == "soltero"):
        print("Es muy pequeño para no ser soltero")

