array = [ 5, 2, 1, 55, 84, 21, 10, 9]

flag = False
while flag == False:
    flag = True
    for i in range(len(array)-1):
        if array[i] > array[i + 1]:
            aux = array[i]
            array[i] = array[i+1]
            array[i+1] = aux
            flag = False

print(array)