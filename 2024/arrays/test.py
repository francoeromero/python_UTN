apellidos_comunes = ['López', 'Gómez','Gómez', 'Fernández', 'Pérez', 'Martínez' ]

strings = []
for i in range(len(apellidos_comunes)):
    counter = 0
    last_name = apellidos_comunes[i]
    for j in range(len(apellidos_comunes)):
        if apellidos_comunes[i] == apellidos_comunes[j]:
            last_name == apellidos_comunes[i]
            counter += 1
            
    message = f'{last_name} se repite {counter} veces'
    strings.append(message)

print(strings)