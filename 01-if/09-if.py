# Escribir un programa que le pida al usuario que ingrese una letra, y luego imprima "Es una vocal" si la letra es una vocal (a, e, i, o, u), o "Es una consonante" si la letra es una consonante.

letra = input("Ingrese una letra: ")
if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
    print("Es una vocal")
else:
    print("Es una consonante")