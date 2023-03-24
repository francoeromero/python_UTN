def mostrar():
    edad = input("Ingrese edad: ")
    edad = int(edad)
    if edad < 5:
        print("Usted es un bebe")
    elif edad < 12:
        print("Usted es un niño")
    elif edad < 17:
        print("Usted es un adolescente")
    elif edad < 50:
        print("Usted es adulto")
    else:
        print("Usted es un anciano")
mostrar()