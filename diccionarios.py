#diccionarios nos permite usar por una clave 

diccionario = dict(nombre="alumno", plataforma="udemy", edad= "18")
print(diccionario)

print(diccionario["nombre"])


a= diccionario.items()
print(a)
#copy
b= diccionario.copy()
print(b)  # me devuelve una copia exacta  del diccinario 

#key  obtner las llaves de un diccionario 

keys = diccionario.keys()
print(keys) # solo me devuelve las llaves del diccionario.

# values 

values = diccionario.values()
print(values)


# aun diccionario tambien lo  pondemos recorrecorre r con un bucle for 

for n in diccionario.keys():
     print(n +"su valor"+ diccionario[n])

for n in diccionario.keys():
    print("{} su valor es: {}".format(n,diccionario[n])) 