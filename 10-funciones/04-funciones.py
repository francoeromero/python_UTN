# Crear una función que calcule el promedio de edad de un grupo de personas. Recibe una lista de edades y devuelve el promedio.

lista_edades = [19, 18, 20] # suma 57 dividido 3 seria 19 
def promedio_edades(edades):
    promedio =  sum(edades) / len(edades)
    return promedio
print(promedio_edades(lista_edades))