# meses = {
#     "enero": 31,
#     "febrero": 28,
#     "marzo": 31,
#     "abril": 31,
#     "mayo": 30,
#     "junio": 30,
#     "agosto" : 31,
#     "septiembre": 30,
#     "octubre" : 31,
#     "noviembre" : 30,
#     "diciembre" : 31
#     }
# mes_ingresado = input("Ingrese un mes : ")
# for mes in meses:
#     if(mes_ingresado == mes):
#         print("La cantidad de dias que tiene {} es: {}".format(mes_ingresado, meses[mes]))

meses = [
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre"
    ]
dias = [28, 30, 31]
m = input("Ingrese un mes: ")
for dia in dias: 
    for mes in meses:
        if(m == "febrero" and dia == dias[0]):
            cantidad_dias = dias[0]
            break
        elif((m == "enero" or m == "abril" or m == "junio" or m == "septiembre" or m == "noviembre") and dia == dias[1]):
            cantidad_dias = dias[1]
            break
        else:
            cantidad_dias = dias[2]
            break
print(cantidad_dias)


# for i in dias:
    # if(m == "febrero"):
    #     cantidad_dias = i
    # elif(m == "enero" or m == "abril" or m == "junio" or m == "septiembre" or m == "noviembre"):
    #     cantidad_dias = i
    # else:
    #     cantidad_dias = i
# print("La cantidad de dias de {} es {}".format(m, cantidad_dias))

# for i in meses:
#     if(i == "febrero"):
#         cantidad_dias = dias[0]
#     elif(i == "enero" or i == "abril" or i == "junio" or i == "septiembre" or i == "noviembre"):
#         cantidad_dias = dias[1]
#     else:
#         cantidad_dias = dias[2]

# # Declaro las variables
# mes = None
# mensaje = None
# # pido al usuario que ingrese un mes
# mes = input("Ingrese un mes: ")
# # clasifico a que instruccion pertenece el mes ingresado
# match mes:
#     case "febrero":
#         mensaje = "Tiene 28 dias"
#     # case "enero" | case "abril" | case "junio" | case "septiembre" | case "noviembre":
#         mensaje = "Tiene 30 dias"
#     case _:
#         mensaje = "Tiene 31 dias"
# # muestro en consola
# print("El mes {} {}".format(mes, mensaje))



