from data_stark import lista_personajes

def extraer_iniciales (nombre_heroe):
    iniciales = ""
    nombre_heroe = nombre_heroe.replace("the", "")
    nombre_heroe = nombre_heroe.replace("-", " ")
    nombre_heroe = nombre_heroe.split(" ")

    for heroe in nombre_heroe:
        if heroe == " ":
            iniciales = "N/A" 
        else: 
            iniciales += heroe[:1] 
            iniciales = ".".join(iniciales)
    #print(iniciales)
    return iniciales

def listar_iniciales(heroe):
    lista = []
    for i in heroe:
        lista.append(extraer_iniciales(i["nombre"]))
        juntar = ". ".join(lista)
    print(juntar)


# def menu():

#     print("opcion 1")
#     print("opcion 2")
#     print("opcion 3")
#     print("opcion 4")
#     print("opcion 5")
#     print("opcion 6")
#     print("opcion 7")
#     print("opcion 8")
#     print("opcion 9: Salir")

#     opcion = input("elije una opcion: ")

#     return opcion

def menu():

    print("1. opcion 1 ")
    print("2. opcion 2")
    print("3. opcion 3")
    print("4. opcion 4")
    print("5. salir")

    opcion = input("Eliga una opcion: ")

    return opcion

continuar = True

while continuar:

    opciones = menu()

    match opciones:
        case "1":

            listar_iniciales(lista_personajes)
            #print("Eligio opcion 1")
            input("Presione una tecla para continuar")
        case "2":
            #print("Eligio opcion 2")
            input("Presione una tecla para continuar")
        case "3":
            #print("Eligio opcion 3")
            input("Presione una tecla para continuar")
        case "4":
            #print("Eligio opcion 4")
            input("Presione una tecla para continuar")
        case "5":
            #print("chau")
            continuar = False

"""
ejercio 1

Crear la función ‘extraer_iniciales’ que recibirá como parámetro: 
nombre_heroe: un string con el nombre del personaje
La función deberá devolver a partir del parámetro recibido un nuevo string con 
las iniciales del nombre del personaje seguidos por un punto (.)
En el caso que el nombre del personaje contenga el artículo ‘the’ se 
deberá omitir de las iniciales
Se deberá verificar si el nombre contiene un guión ‘-’ y sólo en el caso 
que lo tenga se deberá reemplazar por un espacio en blanco
La función deberá validar:
Que el string recibido no se encuentre vacío
Devolver ‘N/A’ en caso de no cumplirse la validación
Ejemplo de la salida de la función para Howard the Duck:
H.D.
"""
# def extraer_iniciales(nombre_heroe):
#     iniciales = " "
#     nombre_heroe = nombre_heroe.replace("the", " ")
#     nombre_heroe = nombre_heroe.replace("-", " ")
#     for i in nombre_heroe:
#         if i["nombre"] == " ":
#             iniciales = "N/A"
#         else:
#             iniciales = iniciales + i[:1]
#     print(iniciales)




# continuar = True
# while(continuar):
#     opcion_elegida = menu()
#     match(opcion_elegida):
#         case "1":
#             # print("elegiste opcion 1")
#             extraer_iniciales(lista_personajes)
#             # input("presione una tecla para continuar")
#         case "2":
#             print("elegiste opcion 2")
#         case "3":
#             print("elegiste opcion 3")
#         case "4":
#             print("elegiste opcion 4")
#         case "5":
#             print("elegiste opcion 5")
#         case "6":
#             print("elegiste opcion 6")
#         case "7":
#             print("elegiste opcion 7")
#         case "8":
#             print("elegiste opcion 8")
#         case "9":
#             continuar = False


