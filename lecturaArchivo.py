# para la lectura de un archivo 
archivo = open("wordlist.lst","r") # para la lectura de un archivo

#print(archivo.readlines()) # para leer el archivo 

for l in archivo.read().split("\n"): # para ler archivos palabra por palabra 
    print(l)
    

lista = archivo.read().split("\n")

print(lista )