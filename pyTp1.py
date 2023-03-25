def sumar():
    precioUno = input("Ingrese primer numero: ")
    precioUno = float(precioUno)
    precioDos = input("Ingrese otro numero: ")
    precioDos = float(precioDos)
    precioTres = input("Ingrese otro: ")
    precioTres = float(precioTres)
    resultado = precioUno + precioDos + precioTres
    resultado = str(resultado)
    print("El resultado de la suma es " + resultado)
sumar()
def promedio():
    precioUno = input("Ingrese primer numero: ")
    precioUno = float(precioUno)
    precioDos = input("Ingrese otro numero: ")
    precioDos = float(precioDos)
    precioTres = input("Ingrese otro: ")
    precioTres = float(precioTres)
    resultado = precioUno + precioDos + precioTres
    promedio = resultado / 3
    promedio = str(promedio)
    print("El resultado del promedio es " + promedio)
promedio()
def precioFinal():
    precioUno = input("Ingrese primer numero: ")
    precioUno = float(precioUno)
    precioDos = input("Ingrese otro numero: ")
    precioDos = float(precioDos)
    precioTres = input("Ingrese otro: ")
    precioTres = float(precioTres)
    resultado = precioUno + precioDos + precioTres
    precioFinal = resultado * 1.21
    precioFinal = str(precioFinal)
    print("El precio final + IVA es " + precioFinal)
precioFinal()