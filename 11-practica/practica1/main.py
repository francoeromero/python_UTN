# FORMAS DE IMPORTAR 
# 1 - import archivo
# import aritmeticas

# print(aritmeticas.sumar(4, 7)) 
# print(aritmeticas.restar(3, 2))

# 2 - from archivo import funcion, funcion
from aritmeticas import sumar, restar
# 3 - from carpeta.archivo import funcion
from modulos.saludos import decir_hola

print(sumar(4, 7))
print(restar(3, 2)) 
decir_hola()        