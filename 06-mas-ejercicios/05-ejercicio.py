# Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
# por cada estadía como base, se pide el ingreso de una estación del
# año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
# Plata/Córdoba) para vacacionar para poder calcular el precio final: -en Invierno:
# Bariloche tiene un aumento del 20% 
# Cataratas y Córdoba tiene un descuento del 10% 
# Mar del Plata tiene un descuento del 20% 
# 
# 
# -en Verano: Bariloche tiene
# un descuento del 20%
#  Cataratas y Córdoba tiene un aumento del 10%
#  Mar delPlata tiene un aumento del 20% 
# 
# -en Otoño y Primavera:
#  Bariloche tiene un aumento del 10% 
# Cataratas tiene un aumento del 10% 
# Mar del Plata tiene unaumento del 10% y
#  Córdoba tiene el precio sin descuento.
# Validar el ingreso de datos

estadia = 15000
descuento = 0
aumento = 0
estacion = input("Ingrese estacion : ")
while(estacion != "invierno" and estacion != "verano" and estacion != "otoño" and estacion != "primavera"):
    estacion = input("ERROR! reingrese la estacion: ")
localidad = input("Ingrese localidad: ")
while(localidad != "bariloche" and localidad != "cataratas" and localidad != "mar del plata" and cordoba != "cordoba"):
    localidad = input("ERROR! reingrese localidad: ")

if(estacion == "invierno"):
    if(localidad == "bariloche"):
        aumento = 0.2
    elif(localidad == "cataratas" or localidad == "cordoba"):
        descuento = 0.1
    elif(localidad == "mar del plata"):
        descuento = 0.2
elif(estacion == "verano"):
    if(localidad == "bariloche"):
        descuento = 0.2
    elif(localidad == "cataratas" or localidad == "cordoba"):
        aumento = 0.2
    elif(localidad == "mar del plata"):
        aumento = 0.1
else:
    if(localidad == "bariloche" or localidad == "cataratas" or localidad == "mar del plata"):
        aumento = 0.1
descuento_total = estadia * descuento
aumento_total = estadia * aumento
precio_final = estadia - descuento_total + aumento_total
print("su precio final es : {}".format(precio_final))