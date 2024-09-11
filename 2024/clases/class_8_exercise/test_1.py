list = [['12345678', 'Rocky', 5, 'Dog', 'Male', 12.1, '30/04/2024', 'Revision dental'],
    ['123', 'Coco', 2, 'Cat', 'Female', 4.8, '03/05/2024', 'Desparasitacion'],
    ['12345678', 'Rocky', 5, 'Dog', 'Male', 12.1, '30/04/2024', 'Revision dental'],
    ['12345678', 'Rocky', 5, 'Dog', 'Male', 12.1, '30/04/2024', 'Revision dental']]

def show_history(list):
    dni = input('ingrese el dni del dueño de la mascota: ')
    for i in range(len(list)):
        if list[i][0] == dni:
            pet_found = i
            break
    return pet_found
            
print(show_history())


# historial_medico = {'2/2/2002' : ''}
# list[0].append(historial_medico)
