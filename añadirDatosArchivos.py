
archivo = open("archivo1.txt","a")
profesion = raw_input("ddedicacion")
empresa = raw_input("Empresa:")
idioma = raw_input("idioma:")

archivo.write(profesion)
archivo.write("\n")
archivo.write(empresa)
archivo.write("\n")

archivo.write(idioma)
archivo.write("\n")

archivo.close()