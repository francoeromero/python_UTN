
# inicializar lista principal
lista_alumnos = []

# usamos for porque son solo 10 estudiantes especificamente
for i in range(2):
    # print salto de linea
    print('')
    # pedimos al usuario los datos
    nombre = input('ingrese nombre: ')
    edad = input('ingrese edad: ')
    while int(edad) < 0 or int(edad) > 99 :
        edad = input('ingrese edad correctamente: ')
    edad = int(edad)
    dni = input('ingrese dni: ')
    while int(dni) <= 99999999:
        dni = input('ingrese dni: ')
    dni = int(dni)
    genero = input('ingrese genero: ').upper()
    while genero != 'M' and genero != 'F' and genero != 'NB':
        genero = input('ingrese genero: ').upper()
    nota = int(input('ingrese nota: '))
    while nota < 1 or nota > 10:
        nota = int(input('ingrese nota: '))
    # creamos la sublista para meter a todas estas variables que el usuario coloco el valor
    lista_datos = [nombre,edad,dni,genero,nota]
    # y luego lo metemos en la lista principal
    lista_alumnos.append(lista_datos)

print(lista_alumnos)

# 1. Listado de todos los alumnos con un formato similar al siguiente:
#     || Juan || 22 || 2020202020 ||  M ||  5 ||
#     || Alma || 20 || 3222332323 ||  F ||  3 ||  

# for i in range(len(lista_alumnos)):
#     print(f'|| {lista_alumnos[i][0]} || {lista_alumnos[i][1]} || {lista_alumnos[i][2]} || {lista_alumnos[i][3]} || {lista_alumnos[i][4]} ||')
message = '|| '
for i in range(len(lista_alumnos)):
    for j in range(len(lista_alumnos[i])):
        message += f'{lista_alumnos[i][j]} || '
print(message)