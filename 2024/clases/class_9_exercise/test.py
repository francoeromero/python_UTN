

# alphabet = ['basddsa','asdadasdsa','cdsasda','vdsasda','zdsadsa','hdsasad']
# print(alphabet)
# for i in range(len(alphabet)):
#     for j in range(i+1,len(alphabet),1):
#         if alphabet[i] > alphabet[j]:
#             aux = alphabet[i]
#             alphabet[i] = alphabet[j]
#             alphabet[j] = aux
# print(alphabet)


# names = ['basfdfsda','asfdfs','c','vds','za','hdsasad']
# print(names)

# for i in range(len(names)):
#     for j in range(i+1,len(names),1):
#         if len(names[i]) > len(names[j]):
#             aux = names[i]
#             names[i] = names[j]
#             names[j] = aux
    
# print(names)


array = [
    ['franco','rodriguez'],
    ['ezequiel','gomez'],
    ['alan','alarcon']
    ]
prioriting_sorting = 'name'
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
            