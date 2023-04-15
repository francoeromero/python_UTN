
num = input("Ingrese un numero del 0 al 9: ")
num = int(num)

while num < 0 or num > 9:
    num = input("ERROR! Tiene que ser del 0 al 9: ")
    num = int(num)
print("CORRECTO!") 

