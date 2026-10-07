#Leer un archivo llamado datos.txt
archivo = open("datos.txt", "r")
# "r" es para que sea solo lectura
#el nombre de la variable es archivo pero puede tener cualquier mombre
print(archivo.read())
archivo.close 

archivomisdatos = open("misdatos.txt", "r")
print(archivomisdatos.read())
archivo.close