# Dado un número entero n, imprimir si el número es primo o no.

# pido numero 
n_ingresado = input("Ingrese su numero: ")
n = int(n_ingresado)
# inicializacion 
es_primo = True
# divisor
i = 2
# el divisor sea menor que el numero 
while i < n: 
    # si el resto de la division es cero
    if (n % i == 0):
        es_primo = False
        break # sale de la iteracion
    else:
    i = i + 1 

if(es_primo and n > 1):
    print("es primo")
else:
    print(" No es primo")