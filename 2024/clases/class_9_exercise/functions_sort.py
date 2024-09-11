'''
#descendiente
num = [5,3,1,7,9]
print(num)
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i] < num[j]:
            aux = num[i]
            num[i] = num[j]
            num[j] = aux 
print(num)
#[5, 3, 1, 7, 9]
#[9, 7, 5, 3, 1]
#------------------------------
# ascendente
print(num)
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i] > num[j]:
            aux = num[i]
            num[i] = num[j]
            num[j] = aux 
print(num)
#[5, 3, 1, 7, 9]
#[1, 3, 5, 7, 9]
'''
'''
 1- Realizar una función que ordene una lista de entero en orden ascendente o
 descendente dependiendo de un parámetro que se le envíe, la función debe retornar
 la cantidad de cambios que se realizaron.
'''
def sort_array(array:list,order:bool)->int:
    change_counter = 0
    if order == True:
        # ascendant
        for i in range(len(array)):
            for j in range(i+1,len(array)):
                if array[i] > array[j]:
                    change_counter += 1
                    aux = array[i]
                    array[i] = array[j]
                    array[j] = aux
    elif order == False:
        # descendant
        for i in range(len(array)):
            for j in range(i+1,len(array),1):
                if array[i] < array[j]:
                    change_counter += 1
                    aux = array[i]
                    array[i] = array[j]
                    array[j] = aux
    return change_counter

sort_array([5, 3, 1, 7, 9],True)

'''
 2- Realizar una función que ordene una lista de nombres de la A-Z o viceversa
 dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad
 de cambios que se realizaron.
'''
def sort_names_alphabetically(names:list):
    change_counter = 0
    for i in range(len(names)):
        for j in range(i+1,len(names)):
            if names[i] > names[j]:
                change_counter += 1
                aux = names[i]
                names[i] = names[j]
                names[j] = aux
    return change_counter

def sort_names_length(names:list):
    change_counter = 0
    for i in range(len(names)):
        for j in range(i+1,len(names),1):
            if len(names[i]) > len(names[j]):
                change_counter += 1
                aux = names[i]
                names[i] = names[j]
                names[j] = aux
    return change_counter


def sort_name_lastname(array:list,prioriting_sorting:str):
    if prioriting_sorting == 'name':
        for i in range(len(array)):
            for j in range(i+1,len(array),1):
                if array[i][0] > array[j][0]:
                    aux = array[i][0]
                    array[i][0] = array[j][0]
                    array[j][0] = aux
    elif prioriting_sorting == 'lastname':
        for i in range(len(array)):
            for j in range(i+1,len(array),1):
                if array[i][1] > array[j][1]:
                    aux = array[i][1]
                    array[i][1] = array[j][1]
                    array[j][1] = aux 
    else:
        return 'Error, write the parameters correctly'
    return array