'''
El programa debe permitir al usuario ingresar los siguientes datos para 10 alumnos:
● Nombre
● Edad
● DNI
● Género (M para masculino, F para femenino, NB para No Binario)
● Nota
Después de ingresar los datos de todos los alumnos, el programa debe calcular y
mostrar la siguiente información:
1. Listado de todos los alumnos con un formato similar al siguiente:
    || Juan || 22 || 2020202020 ||  M ||  5 ||
    || Alma || 20 || 3222332323 ||  F ||  3 ||   
2. El promedio de edades de los alumnos.
3. La cantidad de alumnos que promocionaron (nota mayor o igual a 6).
4. La cantidad de alumnos que aprobaron (nota mayor o igual a 4).
5. La cantidad de alumnos que desaprobaron (nota menor a 4).
6. El promedio de nota de los alumnos masculinos.
7. El porcentaje de alumnas que promocionaron sobre el total de alumnas.
'''

message_of_list = '\n'
number_students = 3
array_students = []
information = ['name', 'age','dni', 'gender','test score']
acumulate_ages = 0
test_grater_than_six = 0
test_grater_than_four = 0
test_less_than_four = 0
# 6 and 7
count_male_high_score = 0
count_female_high_score = 0
total_female = 0
total_male = 0
total_female_high_score = 0
total_male_high_score = 0 
acumulate_male_score = 0

for i in range(number_students):
    array_student = []
    for j in range(len(information)):
        data = input(f'Enter the {information[j]} of student: ')
        
        if information[j] == 'name':
            while data.isdigit():
                data= input(f'Enter correctly the {information[j]} of student: ')

        elif information[j] == 'age':
            while not data.isdigit() or int(data) < 0 or int(data) > 100:
                data= input(f'Enter correctly the {information[j]} of student: ')
            data = int(data)
            # 2
            acumulate_ages += data

        elif information[j] == 'dni':
            while not data.isdigit() or len(data) != 8:
                data= input(f'Enter correctly the {information[j]} of student: ')
            data = int(data)

        elif information[j] == 'gender':
            while data.upper() != 'M' and data.upper() != 'F' and data.upper() != 'NB':
                data= input(f'Enter correctly the {information[j]} of student: ').upper()


        elif information[j] == 'test score':
            while data.isalpha() or int(data) < 0 or int(data) > 10:
                data= input(f'Enter correctly the {information[j]} of student: ')
            data = int(data)

            # 3
            if data > 5 :
                test_grater_than_six += 1
            elif data > 3:
                test_grater_than_four += 1 
            elif data < 4:
                test_less_than_four += 1
            
        array_student.append(data)
        # 1.
        if information[j]=='test score':
            message_of_list += f' {data} \n'
        else:
            message_of_list += f' {data} ||'
    array_students.append(array_student)

# 2
average_age = acumulate_ages / number_students
# 6. El promedio de nota de los alumnos masculinos
for i in range(len(array_students)):
    # 7
    if array_students[i][3].upper() == 'M':
        total_male += 1
        # 6
        acumulate_male_score += array_students[i][4]
        if array_students[i][4] > 5:
            count_male_high_score += 1
    elif array_students[i][3].upper() == 'F':
        total_female += 1
        if array_students[i][4] > 5:
            count_female_high_score  += 1

# 6 
if total_male > 0:
    average_m = acumulate_male_score / total_male
else:
    average_m = 0
# 7. 
if total_male > 0:
    porcentege_m = (count_male_high_score * 100) / total_male
else:
    porcentege_m = 0

if total_female > 0:
    porcentege_f = (count_female_high_score * 100) / total_female
else:
    porcentege_f = 0



print('REGISTER OF STUDENTS')
print(message_of_list)
print(f'2. The average age of students is: {average_age}')
print(f'3. The number of students with test score greater than 6 is: {test_grater_than_six}')
print(f'4. The number of students who passed with a score of 4 or higher: {test_grater_than_four}')
print(f'5. The number of students who failed : {test_less_than_four}')
print(f'6. The average grade point of male students : {average_m}')
print(f'7. The porcentege of male studients with high score is : {porcentege_m}')
print(f'7. The porcentege of female studients with high score is : {porcentege_f}')




