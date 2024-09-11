'''

En una veterinaria se están realizando censos para evaluar los animales ingresados por día. Por este motivo, se le realizará una consulta al menos 6 clientes.

Se requieren los siguientes datos:
Tamaño de la mascota (Chica, Mediana o Grande).
Sexo de la mascota (Hembra o Macho).
Tipo de mascota (Gato, Perro, Otro).
Edad de la mascota. Validar.
Está vacunado? SI/NO (Se puede utilizar boolean si se desea).
INFORMAR


A- Cuál es el tipo, el sexo y la edad de la mascota más joven entre los tamaños medianos o grandes.
B- Cuál es el promedio de edad de los PERROS.
C- Cuál es el tipo de mascota más vacunado.

'''

flag = 0
acumulate_age = 0
pets = 6
count_age_dog  = 0
count_dog = 0
count_cat = 0
count_other = 0
for i in range(0,pets):
    size_pet = input('Enter the size of the pet:(small/ medium / large):').lower()
    while size_pet != 'small' and size_pet != 'medium' and size_pet != 'large':
        size_pet = input('Enter the size pet correctly: (small/ medium / large)')

    gender_pet = input('Enter the gender of the pet(male / female): ').lower()
    while gender_pet != 'male' and gender_pet != 'female':
        gender_pet = input('Enter correctly gender of the pet (female or male):')
    
    type_pet = input('Enter the type of the pet:(cat/ dog / other):').lower()
    while type_pet != 'cat' and type_pet != 'dog' and type_pet != 'other':
        type_pet = input('Enter the size pet correctly: (cat/ dog / other)')
    
    age_pet = input('Enter the age of the pet: ')
    while age_pet.isalpha() or int(age_pet)<0:
        age_pet = input('Enter correctly the age of the pet: ')
    age_pet = int(age_pet)

    vaccinated = input('Is the dog vaccinated?(Enter y/n)').lower()
    while vaccinated != 'y' and vaccinated != 'n':
        vaccinated = input('Enter only y(YES) or n(NO):')

    # A
    if flag == 0:
        youngest_pet = age_pet
        flag = 1
    elif size_pet == 'medium' or size_pet == 'large':
        if age_pet < youngest_pet:
            youngest_pet = age_pet
            youngest_age = age_pet
            youngest_gender = gender_pet
            youngest_type = type_pet
    # B
    if type_pet == 'dog':
        acumulate_age  += age_pet
        count_age_dog += 1
    # C
    if type_pet == 'cat' and vaccinated == 'y':
        count_cat += 1
    elif type_pet == 'dog' and vaccinated == 'y':
        count_dog += 1
    elif type_pet == 'other' and vaccinated == 'y':
        count_other += 1
# B
average_age_dog = acumulate_age / count_age_dog
# C

if count_cat > count_dog and count_cat > count_other:
    type_pet_most_vaccinated = 'cat'
elif count_dog > count_cat and count_dog > count_other:
    type_pet_most_vaccinated = 'dog'
elif count_other > count_dog and count_other > count_cat:
    type_pet_most_vaccinated = 'other'
else:
    type_pet_most_vaccinated = 'there is not a more vaccinated type of pet, there is an equity' 
    

    