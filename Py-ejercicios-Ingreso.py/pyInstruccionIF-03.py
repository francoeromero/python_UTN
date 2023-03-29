def mostrar():
    edad = input("Ingrese edad: ")
    edad = int(edad)
    if not( edad < 13 or edad > 17):
        print("Usted es adolescente")
    else:
        print("Mayor de edad")
mostrar()