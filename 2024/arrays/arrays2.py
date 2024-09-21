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

print(register(2))