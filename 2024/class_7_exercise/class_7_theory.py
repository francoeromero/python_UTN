# lista_anidada = [[1,2,3],[4,5,6],[7,8,9]]

# # print(lista_anidada)
# print(len(lista_anidada[0]))
# sub_lista = lista_anidada[1]

# print(sub_lista[0]) 
# print(lista_anidada[1][0])
# # 
# lista_usuarios = []
# for i in range(3):
#     for j in range(2):
#         lista_usuario = []
#         dato = input('ingrese el dato: ')
#         lista_usuario.append(dato)
#     lista_usuarios.append(lista_usuario)

# print(lista_usuarios)

# 1. other alternative 
# for i in range(len(array_students)):  
#     print(f'|| {array_students[i][0]} || {array_students[i][1]} || {array_students[i][2]} || {array_students[i][3]} || {array_students[i][4]}')

acumulate_m = 0
count_m  = 0
acumulate_m = 0
count_m_average = 0
count_male_high_score = 0
count_female_high_score = 0
array_students = [[1,1,1,'M',6],[1,1,1,'M',7],[1,1,1,'F',8]]

# print(array_students[0][4])
for i in range(len(array_students)):
    if array_students[i][4] > 5 :
        if array_students[i][3] == 'M':
            count_male_high_score += 1
        elif array_students[i][3] == 'F':
            count_female_high_score += 1
porcentege_m = (count_male_high_score * 100) / 3
porcentege_f = (count_female_high_score * 100) / 3
print(f'cantidad f: {count_female_high_score}')
print(f'cantidad m: {count_male_high_score}')
print(f'% f {porcentege_m}')
print(f'% m {porcentege_f}')



# for i in range(len(array_students)):
#     if array_students[i][3] == 'M':
#         acumulate_m += array_students[i][4]
#         count_m += 1
# average_m = acumulate_m / count_m
# print(average_m)