import os
from funciones import *

def menu():
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        opcion = int(input("Su opcion: "))
        
        if opcion == 1:
            a = ingresar_primer_operando()
        elif opcion == 2:
            b = ingresar_segundo_operando()
        elif opcion == 3:
            resultado_suma = calcular_suma(a,b)
            resultado_resta = calcular_resta(a,b)
            resultado_division = calcular_division(a,b)
            resultado_multiplicacion = calcular_multiplicacion(a,b)
            resultado_potencia = calcular_potencia(a,b)
            resultado_resto = calcular_resto(a,b)
            resultado_factorial = calcular_factorial(a)
        elif opcion == 4:
            print("Resultado suma: ",resultado_suma)
            print("Resultado resta: ",resultado_resta)
            print("Resultado division: ",resultado_division)
            print("Resultado multiplicacion: ",resultado_multiplicacion)
            print("Resultado potencia: ",resultado_potencia)
            print("Resultado resto: ",resultado_resto)
            print("Resultado factorial: ", resultado_factorial)
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
        input("Pulse boton para continuar...")
        os.system('clear')

    
    
menu()
