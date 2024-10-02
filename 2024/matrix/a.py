def porcentajes(lista_nombres:list,lista_valores:list):
    total = sum(lista_valores)
    porcentajes = []
    mensaje = ''
    if len(lista_nombres) == len(lista_valores):
        for i in range(len(lista_valores)):
            resultado = (lista_valores[i] * 100) / total
            porcentajes.append(resultado)
            mensaje += f'{lista_nombres[i]}: {resultado} % '
        return mensaje
    else:
        return 'las listas tienen que ser equitativas'


def porcentaje_alumnos(matriz:list):
    fem = 0
    masc = 0
    nob = 0
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            if col == 3:
                if matriz[fil][col] == 'f':
                    fem += 1
                elif matriz[fil][col] == 'm':
                    masc += 1
                else:
                    nob += 1
    lista_cantidad_generos = [fem,masc,nob]
    lista_generos = ['femeninos', 'masculinos', 'no binarios']
    mensaje = porcentajes(lista_generos, lista_cantidad_generos)
    return mensaje

una_matriz =[['jorgito', 'romero', 3,'m'],['jorgito', 'romero', 3,'f'],['jorgito', 'romero', 3,'nb']]
print(porcentaje_alumnos(una_matriz))