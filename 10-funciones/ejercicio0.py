from data_stark import lista_personajes

def menu():

    print("opcion 1")
    print("opcion 2")
    print("opcion 3")
    print("opcion 4")
    print("opcion 5")
    print("opcion 6")
    print("opcion 7")
    print("opcion 8")
    print("Salir")

    opcion = input("elije una opcion: ")

    return opcion

continuar = True

while(continuar):
    opcion_elegida = menu()
    match(opcion_elegida):
        case "1":
            print("elegiste opcion 1")
            input("presione una tecla para continuar")
        case "2":
            print("elegiste opcion 2")
        case "3":
            print("elegiste opcion 3")
        case "4":
            print("elegiste opcion 4")
        case "5":
            print("elegiste opcion 5")
        case "6":
            print("elegiste opcion 6")
        case "7":
            print("elegiste opcion 7")
        case "8":
            print("elegiste opcion 8")
        case "9":
            continuar = False
