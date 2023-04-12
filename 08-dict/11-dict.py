# Crea un diccionario que represente una lista de tareas por hacer. Cada clave del diccionario debe ser el nombre de una tarea y cada valor debe ser su estado (los estados son:  pendiente, en proceso, completada). Imprimir todas las tareas seguido de su estado

lista_de_tareas = {
    "gimnasio" : "pendiente",
    "estudiar" : "en proceso",
    "salir a bailar" : "pendiente",
    "recibir mi certificado" : "completada"
}
for i in lista_de_tareas:
    print(i, lista_de_tareas[i])