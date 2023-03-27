def rectangulo():
    anchoIngresado = input("Ingrese la medida del ancho: ")
    anchoIngresado = float(anchoIngresado)
    largoIngresado = input("Ingrese la medida del largo: ")
    largoIngresado = float(largoIngresado)
    perimetro = (anchoIngresado + largoIngresado)*2
    alambre = 3 * perimetro
    alambre = str(alambre)
    perimetro = str(perimetro)
    print("La cantidad de alambre es " + alambre + " metros")
    print("El perimetro es de : " + perimetro + " metros")
rectangulo()