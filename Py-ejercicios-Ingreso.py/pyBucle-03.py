def mostrar():
    clave = "utn750"
    clave = input("Ingrese la contraseña: ").lower()
    while clave != "utn750":
        clave = input("clave incorrecta vuelva a escribir: ").lower()
mostrar()
print("CLAVE CORRECTA!")
