'''
1. Escribir una función que reciba como parámetro una lista de str y cuente la cantidad de elementos con más de cinco caracteres.
Para contar los caracteres de un string también se usa la función len

'''

def array_string(strings:list):
    counter= 0 
    for i in range(len(strings)):
        if len(strings[i]) > 4:
            counter += 1
    return counter


'''
2. Escribir una función que reciba como parámetro una lista de str y retorne una nueva lista con los elementos de más de cinco caracteres.

'''
def array_more_than_five_characters(strings:list):
    new_array = []
    for i in range(len(strings)):
        if len(strings[i]) > 4:
            new_array.append(strings[i])
    return new_array

# hola = ['asd', 'asddasdasdasdas', 'asasddas']

# print(array_more_than_five_characters(hola))


'''
3. Escribir una función que me permita ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Retornar una lista con el/los nombres de la personas con el nombre más corto (tener en cuenta más de un mínimo)
'''

def register(number_people:int):
    new_array = []
    for i in range(number_people):
        person = input('Enter the name of person: ')
        while person.isdigit():
            person = input('Enter correctly the name of person: ')
        new_array.append(person)
        
        if i == 0 or len(person) < len(the_shortest_name):
            the_shortest_name = person

    
    message = f'list: {new_array} \n the shortest name: {the_shortest_name}'
    return message

'''
4. Escribir una función que reciba una lista de apellidos comunes como esta:
apellidos_comunes = [“López”, “Gómez”, “Fernández”, “Pérez”, “Martínez” ]
Ingresar 10 apellidos y guardarlos en otra lista. Contar cuantas veces se repiten los apellidos comunes.

Ejemplo
López se repite 2 veces
Gómez se repite 0 veces
Fernández se repite 1 vez
Pérez se repite 0 veces
Martínez se repite 3 veces

'''
apellidos_comunes = ['López', 'Gómez','Gómez', 'Fernández', 'Pérez', 'Martínez' ]
def organize_last_names(array_last_names:list):
    strings = []
    for i in range(len(array_last_names)):
        counter = 0
        last_name = array_last_names[i]
        for j in range(len(array_last_names)):
            if array_last_names[i] == array_last_names[j]:
                last_name == array_last_names[i]
                counter += 1
                
        message = f'{last_name} se repite {counter} veces'
        strings.append(message)
    return strings

# print(organize_last_names(apellidos_comunes))
'''
5.Escribir un programa que me permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años). Utilizar listas paralelas.
(Hacer dos funciones, una para la carga de productos y otra para mostrarlos)

'''
def validate_age(message:str, message_bug:str, min:int, max:int):
    age = input(message)
    while age.isalpha() or int(age) < min or int(age) > max:
        age = input(message_bug)
    age = int(age)
    return age  

def validate_name(message:str, message_bug:str):
    name = input(message)
    while name.isdigit() :
        name = input(message_bug)
    return name

def load_data():
    array = []
    for i in range(0,5,1):
        sub_array = []
        person = validate_name('Enter the name: ', 'Enter correctly name: ')
        age = validate_age('Enter the age: ', 'Enter correctly age: ', 0, 100)
        sub_array.append(person)
        sub_array.append(age)
        array.append(sub_array)
    return array

def show_data():
    new_array = load_data()
    array_over_18_years = []
    for i in range(len(new_array)):
        if new_array[i][1] >= 18:
            array_over_18_years.append(new_array[i])
    return array_over_18_years

# print(show_data())


'''
6. Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Mostrar la cantidad de productos que tienen un precio mayor al primer producto ingresado.
(Hacer dos funciones, una para la carga de productos y otra para mostrarlos)

'''




'''
7. La utn fra necesita un sistema saber la nota promedio más alta entre 5 alumnos de la Materia Programación I. 
Para eso debemos guardar.

Nombre (Ingresa usuario)
Apellido (Ingresa usuario)
Legajo (Ingresa usuario entre 10000 y 99999)
Nota primer parcial (Número aleatorio entre 1 y 10)
Nota segundo parcial (Número aleatorio entre 1 y 10)

Aparte de saber cuál fue esa nota debemos mostrar cuál fue el alumno, en caso de haber más de un alumno con la misma nota promedio mostrar a los dos.

'''