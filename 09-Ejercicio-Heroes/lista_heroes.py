from data_stark import lista_personajes

def menu():
    print("B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe")
    print("C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo")
    print("D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)")
    print("E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)")
    print("F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)")
    print("G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)")
    print("H. Calcular e informar cual es el superhéroe más y menos pesado.")
    print("I. Ordenar el código implementando una función para cada uno de los valores informados")
    print("J. Construir un menú que permita elegir qué dato obtener")
    print("K. SALIR")
    opcion = input("Ingrese una opcion: ")
    return opcion

continuar = True
while(continuar):
    opcion = menu()
    if(opcion == "k"):
        print("Chau")
        continuar = False
    elif(opcion == "b"):
        for i in lista_personajes:
            print(i["nombre"])
    elif(opcion == "c"):
        for i in lista_personajes:
            print(i["nombre"], i["altura"])
    elif(opcion == "d"):
        superheroe_mas_alto = lista_personajes[0]["nombre"] #solo si en la lista son numeros enteros
        maxima_altura = lista_personajes[0]["altura"]
        for i in lista_personajes:
            # maxima_altura = ""
            # bandera = 0
            if(i["altura"] > maxima_altura):
                maxima_altura = i["altura"]
                superheroe_mas_alto = i["nombre"]
            # if(i["altura"] > maxima_altura or bandera == 0):
            #     maxima_altura = i["altura"]
            #     superheroe_mas_alto = i["nombre"]
            #     bandera = 1
            
        print("El superheroe mas alto es {} con una altura de: {} ".format(superheroe_mas_alto,maxima_altura))