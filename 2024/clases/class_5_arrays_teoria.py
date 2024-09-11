lista_edades = [20,18,30,40,35]
lista_facultades = ["UTN","UBA","UNDAV","UADE"]

#Busca la primer ocurrencia de la edad a buscar (Aplicable a varios lenguajes)
def buscar_edad(lista_edades:list,edad_a_buscar:int) -> int:
    retorno = -1#Por defecto está en -1 ya que no existe un indice que sea -1 en varios lenguajes
    
    #For range
    for i in range(len(lista_edades)):
        if lista_edades[i] == edad_a_buscar:
            retorno = i
            break
        
    return retorno
    
#Busca la primer ocurrencia de la edad a buscar (Aplicable a python solamente)
def buscar_edad_python(lista_edades:list,edad_a_buscar:int):
    retorno = False#Por defecto está en false ya que si retorna false significa que no hay una edad cargada en la lista.
               
    #Foreach
    for edad in lista_edades:
        if edad == edad_a_buscar:
            retorno = edad
            break
        
    return retorno

#Busca la primer ocurrencia de la universidad a buscar (Aplicable a varios lenguajes)
def buscar_universidad(lista_facultades:list,facultad_a_buscar:str) -> int:
    retorno = -1#Por defecto está en -1 ya que no existe un indice que sea -1 en varios lenguajes
    
    #For range
    for i in range(len(lista_facultades)):
        if lista_facultades[i] == facultad_a_buscar:
            retorno = i
            break
        
    return retorno
    
#Busca la primer ocurrencia de la edad a buscar (Aplicable a python solamente)
def buscar_universidad_python(lista_facultades:list,facultad_a_buscar:str):
    retorno = False#Por defecto está en false ya que si retorna false significa que no hay una universidad cargada en la lista.
               
    #Foreach
    for universidad in lista_facultades:
        if universidad == facultad_a_buscar:
            retorno = universidad
            break
        
    return retorno


#FORMA OTROS LENGUAJES
edad_a_buscar = int(input("Ingrese edad a buscar: "))
indice_edad_encontrada = buscar_edad(lista_edades,edad_a_buscar)

if indice_edad_encontrada != -1:
    edad_encontrada = lista_edades[indice_edad_encontrada]
    print(f"La edad es de {edad_encontrada} y está ubicada en el indice {indice_edad_encontrada}")
else:
    print("EDAD NO ENCONTRADA")

# FORMA PYTHON
edad_a_buscar = int(input("Ingrese edad a buscar: "))
edad_encontrada = buscar_edad_python(lista_edades,edad_a_buscar)

if edad_encontrada != False:
    print(f"Encontrado el dato. La edad es de {edad_encontrada}")
else:
    print("EDAD NO ENCONTRADA")

    
#FORMA OTROS LENGUAJES
universidad_a_buscar = input("Ingrese universidad a buscar: ")
indice_universidad_encontrada = buscar_universidad(lista_facultades,universidad_a_buscar)

if indice_universidad_encontrada != -1:
    universidad_encontrada = lista_facultades[indice_universidad_encontrada]
    print(f"La universidad es {universidad_encontrada} y está ubicada en el indice {indice_universidad_encontrada}")
else:
    print("UNIVERSIDAD NO ENCONTRADA")

# FORMA PYTHON
universidad_a_buscar = input("Ingrese universidad a buscar: ")
universidad_encontrada = buscar_universidad_python(lista_facultades,universidad_a_buscar)

if universidad_encontrada != False:
    print(f"Encontrado el dato. La universidad es {universidad_encontrada}")
else:
    print("UNIVERSIDAD NO ENCONTRADA")
'''

range(inicio, fin, paso)
Inicio: Es el valor inicial del rango.
Fin: Es el valor final del rango, pero no está incluido.
Paso: Indica cuánto debe aumentar o disminuir el contador en cada iteración.

ejemplo

l1 = [2,4,3]
# for i in range(len(l1),0,-1):
#     print(i)
# 3
# 2
# 1
for i in range(len(l1),-1,-1):
    print(i)
# 3
# 2
# 1
# 0


l1 = [2,4,3]
for i in range(len(l1),-1,-1):
    print(l1[i])
# tira error porque arranca l1[3] y no existe, porque el indice empieza con 0 y el len() enumera desde 1, por eso arranca con l1[3]

corregido seria asi: 
for i in range(len(l1)-1,-1,-1):


interaccion de dos listas 

l1 = [2,4,3]
l2 = [5,6,4]

# for i in range(len(l1)):
#     for j in range(len(l2)):
#         print(f'l1: {l1[i]}')
#         print(f'l2: {l2[j]}')
#         print(f'l1 + l2: {l1[i] + l2[j]}')

# for i in range(len(l1)):
#     print(l1[i] + l2[i])

'''
            