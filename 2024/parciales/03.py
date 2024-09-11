'''
Realizar el algoritmo que permita el ingreso por prompt de las notas (validar entre 0 y 10) , el sexo (validar el sexo “f” o “m”) de 5 alumnos, informar por alert:
a) El promedio de las notas totales.
b) La nota más baja y el sexo de esa persona.
c) La cantidad de varones que su nota haya sido mayor o igual a 6.
'''
students = 5
lowest_grade = 0
sum_grade = 0
flag = 0
count_six_m = 0
for student in range(0,students):

    grade = input('Enter the exam grade (0-10): ')
    while grade.isalpha() or int(grade) < 0 or int(grade) > 10:
        grade = input('Enter the exam grade (0-10): ')
    grade = int(grade)

    gender = input('Enter student s gender(f/m): ').lower()
    while gender.isdigit() or len(gender) != 1 and (gender != 'f' or gender != 'm'):
        gender = input('Gender must be m o f: ')
    # a
    sum_grade += 1 
    # b
    if flag == 0:
        lowest_grade = 0
        gender_lowest_grade = gender
        flag = 1
    elif grade < gender_lowest_grade:
        gender_lowest_grade = grade
    # c
    if gender == 'm' and grade > 5:
        count_six_m += 1
# calculate
average_total_grade = sum_grade / students

print(f'a) El promedio de las notas totales {average_total_grade}')
print(f'b) La nota más baja y el sexo de esa persona. nota: {gender_lowest_grade} sexo: {gender_lowest_grade}')
print(f'c) La cantidad de varones que su nota haya sido mayor o igual a 6: {count_six_m}')
