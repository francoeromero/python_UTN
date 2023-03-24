def mostrar():
    edad = input("Ingrese edad: ")
    edad = int(edad)
    if edad < 5:
        print("Usted es un bebe")
    else:
        if edad < 12:
            print("Usted es un niño")
        else:
            if edad < 17:
                print("Usted es un adolescente")
            else:
                if edad < 50:
                    print("Usted es adulto")
mostrar()