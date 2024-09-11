'''
Programación I
Franco Romero

Para un hospital veterinario

Es necesario registrar el ingreso de las mascotas en la próxima hora (solo se pueden atender 20 mascotas), para esto hay que considerar los siguientes datos y encasillarlos en ciertos diagnósticos para poder derivarlos adecuadamente:

-Edad (Validar entre 1 y 25 años) 

-Tipo: (Validar “gato”, “perro”, “loro”) 

-Peso: (Más de 0 kg) -

-Diagnóstico: (Validar “problemas digestivos”, “parásitos”, “infección”)

-Vacuna antirrábica (validar “si”, ”no”)

CALCULAR

1. Cantidad de mascotas sin vacuna antirrábica, cuya edad está entre los 4 y 12 años, que se presentaron por infección o parásitos.

2. El tipo de mascota más ingresada con problemas digestivos.

3. Edad y tipo de la mascota más vieja con vacuna antirrábica.

4. Porcentaje de mascotas vacunadas y no vacunadas.

5. Promedio de edad de los gatos.
'''

numero_mascotas = 20
contador_infectados = 0
contador_perros_digestivos = 0
contador_gatos_digestivos = 0
contador_loros_digestivos = 0
vacunados = 0
flag_edad = 0
acumulador_edad_gatos = 0
contador_gatos_total = 0
for i in range(0,numero_mascotas):
    print('\nNUEVA MASCOTA')
    # validación
    edad = input('ingrese edad: ')
    while edad.isalpha() or (int(edad) < 1 or int(edad) > 25):
        edad = input('ERROR! ingrese nuevamente: ')
    edad = int(edad)

    tipo = input('ingrese el tipo de mascota(“gato”, “perro”, “loro”): ').lower()
    while tipo != 'gato' and tipo != 'perro' and tipo != 'loro':
        tipo = input('ERROR! solo “gato”, “perro”, “loro”: ').lower()

    peso = input('ingrese el peso de la mascota: ')
    while peso.isalpha() or float(peso) <= 0:
        peso = input('error, reingrese nuevamente: ')
    peso = float(peso)

    diagnostico = input('ingrese el diagnostico “problemas digestivos”, “parásitos”, “infección”: ').lower()
    while diagnostico != 'problemas digestivos' and diagnostico != 'parasitos' and diagnostico != 'infeccion':
        diagnostico = input('error! ingrese correctamente “problemas digestivos” o “parásitos” o “infección”: ').lower()

    vacuna = input('la mascota esta vacunada con la antirrábica? S/N: ').lower()
    while vacuna != 's' and vacuna != 'n':
        vacuna = input('error, solo ingrese S/N: ').lower()

    # 1
    if vacuna == 'n':
        # no vacunados
        if edad >= 4 and edad <= 12 and (diagnostico == 'infeccion' or diagnostico == 'parasitos'):
            contador_infectados += 1
    else:
        # vacunados 
        vacunados += 1
        # 3
        if flag_edad == 0 or edad > edad_mayor:
            edad_mayor = edad
            tipo_mascota_mayor = tipo
            flag_edad = 1
    # 2
    if diagnostico == 'problemas digestivos':
        if tipo == 'gato':
            contador_gatos_digestivos+=1
        elif tipo == 'loro':
            contador_loros_digestivos+=1
        else:
            contador_perros_digestivos+=1
    #5
    if tipo == 'gato':
        acumulador_edad_gatos += edad
        contador_gatos_total += 1
'''
fuera de la iteración
'''
#2
if contador_perros_digestivos > contador_loros_digestivos and contador_perros_digestivos > contador_gatos_digestivos:
    tipo_con_mas_digestivos = 'perro'
elif contador_gatos_digestivos > contador_loros_digestivos and contador_gatos_digestivos > contador_perros_digestivos:
    tipo_con_mas_digestivos = 'gato'
elif contador_loros_digestivos > contador_perros_digestivos and contador_loros_digestivos > contador_gatos_digestivos:
    tipo_con_mas_digestivos = 'loro'
else:
    tipo_con_mas_digestivos = 'iguales'
#4
'''
numero de mascotas = 20
20 _________________100%
vacunados __________ x %
'''
porcentaje_vacunados = (vacunados * 100) / numero_mascotas
porcentaje_no_vacunados = 100 - porcentaje_vacunados #resto

#5
if contador_gatos_total > 0:
    promedio_edad_gatos = acumulador_edad_gatos / contador_gatos_total
else:
    promedio_edad_gatos = 0

print('\n RESULTADO: ')
print(f'1. la cantidad de mascotas sin vacunas antirrabicas entre los 4 y 12 años: {contador_infectados} ')
print(f'2. El tipo de mascota más ingresada con problemas digestivos: {tipo_con_mas_digestivos}')
print(f'3. Edad y tipo de la mascota más vieja con vacuna antirrábica: edad: {edad_mayor}, tipo de mascota: {tipo_mascota_mayor}')
print(f'4. Porcentaje de mascotas vacunadas: {porcentaje_vacunados}% ')
print(f'4. Porcentaje de mascotas no vacunadas: {porcentaje_no_vacunados}% ')
print(f'5. Promedio edad gatos: {promedio_edad_gatos}')