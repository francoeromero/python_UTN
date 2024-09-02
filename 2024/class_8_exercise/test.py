# array = [
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     ['date','history']
#     ]

def validate_dni(dni):
    # lógica de validación para dni
    while dni.isalpha():
        dni = input('Enter correctly dni: ')
    dni = int(dni)
    

def validate_name(name):
    # lógica de validación para name
    pass

validation_functions = {
    'dni': validate_dni,
    'name': validate_name,
    # 'age': validate_age,
    # 'type of pet': validate_type_of_pet,
    # 'gender': validate_gender,
    # 'weight': validate_weight,
    # 'date': validate_date,
    # 'medical history': validate_medical_history
}

new_pet = []
information = ['dni', 'name', 'age', 'type of pet', 'gender', 'weight', 'date', 'medical history']

for key in information:
    data = input(f'Enter {key}:')
    if key in validation_functions:
        validation_functions[key](data)
    new_pet.append(data)