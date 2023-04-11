# Crea una lista de palabras y muestra las palabras que tienen más de 5 letras.

palabras = ["HOLA", "que onda", "Buenas", "ola", "buenas tardes"]
palabras_mas_de_cinco = []

for i in palabras:
    if(len(i) > 5):
        palabras_mas_de_cinco.append(i)
print(palabras_mas_de_cinco)