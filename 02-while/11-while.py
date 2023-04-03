# Dada una lista de palabras, imprimir todas las palabras que tengan una longitud mayor a 5 caracteres.

# palabras = ["hola", "saludos", "buenas", "que tal", "asdasdsaadadsadsdsa"]
# i = 0
# while(len(palabras[i]) > 5):
#     print(palabras[i])
#     i += 1
# correccion: no hay un limite en el while (line 5) por que tenes que mostrarle al while cuantas palabras hay en una lista porque sino va a iterar todo el tiempo pensando que hay infinitas palabras en la lista, ahi solo tenes 5 palabras

# #aca estarias dando un limite de la cantidad de palabras que hay en una lista seria 5 vueltas
# while(len(palabras) >= i):
#     i += 1

palabras = ["hola", "saludos", "buenas", "que tal", "asdasdsaadadsadsdsa"]
i = 0
while(len(palabras) > i):
    if(len(palabras[i]) > 5):
        print(palabras[i])
    i += 1

# palabras = ["hola", "saludos", "buenas", "que tal", "asdasdsaadadsadsdsa"]
# i = 0 
# while(len(palabras) >= i):
#     print(palabras[i]) #  Si i tiene el mismo valor que la longitud de palabras, entonces palabras[i] no existe y se produce un IndexError.
#     i += 1