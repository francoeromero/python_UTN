import datetime
# 1
def register():
    new_pet = []
    information = ['dni', 'name', 'age', 'type of pet', 'gender', 'weight', 'date', 'medical history']
    for i in range(len(information)):
        # sentences
        if information[i] == 'dni':
            data = enter_id('Enter dni: ', 'Enter correctly dni(8 digits): ', 8)
        elif information[i] == 'name':
            data = enter_string('Enter the name: ', 'Enter correctly the name: ')
        elif information[i] == 'age':
            data = range_numbers_integer('Enter age: ', 'Enter correctly age: ', 1, 80)
        elif information[i] == 'type of pet':
            data = options('Enter the type of pet: ', 'Enter correctly (dog/cat/other): ', ['dog', 'cat', 'other'])
        elif information[i] == 'gender':
            data = options('Enter gender: ', 'Enter correctly gender(F/M): ', ['M','F'])
        elif information[i] == 'weight':
            data = range_numbers_float('Enter weight: ', 'Enter correctly weight(0-100)',0,100)
        elif information[i] == 'date':
            data = enter_date()
        elif information[i] == 'medical history':
            data = enter_string('Enter the medical history: ', 'Enter correctly the medical history: ')
        # add sublist
        new_pet.append(data)
    # return sublist
    return new_pet



# sub-functions
def enter_integer(message:str, message_bug:str, min:int)->int:
    data = int(input(message))
    while data < min:
        data = int(input(f'Something went wrong, {message_bug}'))
    return data

def enter_float(message:str, message_bug:str, min:float)->int:
    data = float(input(message))
    while data < min:
        data = float(input(message_bug))
    return data

def enter_date()->str:
    print('DATE')
    day = range_numbers_integer('Enter number  of the day: ','Enter correctly number of the day(1-30): ', 1, 31 )
    month = range_numbers_integer('Enter number of the month: ', 'Enter correctly number of the month (1-12): ', 1, 12)
    year = range_numbers_integer('Enter the number of the year: ', 'Enter correctly the number of the year(2000-2024): ', 2000, 2024)

    date = f'{day}/{month}/{year}'
    return date

def enter_string(message:str,message_bug:str)->str:
    data = input(message).lower()
    while data == '':
        data = input(message_bug)
    return data

def options(message:str, message_bug:str, array_options:list):
    array_lower = []
    for i in range(len(array_options)):
        lower = array_options[i].lower()
        array_lower.append(lower)

    data = input(message)
    while data not in array_lower:
        data = input(message_bug)
    return data

def enter_id(message:str, message_bug:str, lenght:int):
    data = input(message)
    while len(data) < lenght:
        data = input(message_bug)
    data = int(data)
    return data 

def range_numbers_float(message:str, message_bug:str, min:float, max:float):
    data = float(input(message))
    while data < min or data > max:
        data = float(input(message_bug))
    return data 
def range_numbers_integer(message:str, message_bug:str, min:int, max:int):
    data = int(input(message))
    while data < min or data > max:
        data = int(input(message_bug))
    return data 


# 2

def search_pet(array:list):
    name = enter_string('Enter the name of the pet: ', 'Enter correctly name: ')
    index = None
    for i in range(len(array)):
        if array[i][1].lower() == name:
            index = i
            break # so that the iteration does not keep going round and round
    return index

def update(array:list,index:int,history:list):
    #guardamos informacion antes
    sublist = []
    sublist.append(array[index][0]) # dni
    sublist.append(array[index][1]) # name
    sublist.append(array[index][6]) # date
    sublist.append(array[index][7]) # medical history
    history.append(sublist)
    # obtener la fecha de hoy
    date_today = datetime.date.today()
    custom_format = date_today.strftime('%d/%m/%Y')

    date_update = custom_format
    medical_history_update = enter_string('Enter the medical history: ', 'Enter correctly the medical history: ')
    # reemplazo
    array[index][6] = date_update 
    array[index][7] = medical_history_update

def show_history(name:str,array:list):
    hist = ''
    is_there_history = False
    for j in range(len(array)):
        if array[j][1] == name:
            hist += f'{array[j][2]} {array[j][3]} \n'
            is_there_history = True
        else:
            is_there_history = False
            
    if is_there_history == False:
        return 'there is not history'
    else:
        return hist
    
#  3

def average_age_pets(array:list)->float:
    acumulate_age = 0
    for i in range(len(array)):
        acumulate_age += array[i][2]
    average = acumulate_age / len(array) 
    return average


def pets_exceed_average(average:float, array:list)->list:
    array_pets = []
    for i in range(len(array)):
        pet = []
        if array[i][2] > average:
            pet.append(array[i])
            array_pets.append(pet)
    return array_pets
            



















