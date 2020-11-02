archivo = open("archivo1.txt","w")  # nombre del archivo  y modo de escritura 
nombre = raw_input("nombre:")
edad = raw_input("edad:")
pais = raw_input("pais:") 

archivo.write(nombre)
archivo.write("\n")

archivo.write(edad)
archivo.write("\n")

archivo.write(pais )
archivo.write("\n")

print(" se ha escrito en el archivo ")
archivo.close()
