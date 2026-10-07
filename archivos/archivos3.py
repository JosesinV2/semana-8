#Guardar y crear un archivo 
frases = input("Dime tu frase favorita: ")

with open("frases.txt", "w") as archivo:
    archivo.write(frases)

print("archivo creado satisfactorimamet")

#la "w" signica escribir en un archivo
#si el archivo no existe la maquina lo crea

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
carrera = input("Dime la carrera que curdas")

with open("documento.txt", "w") as archivo:
    archivo.write(nombre + "\n")
    archivo.write(edad  + "\n")
    archivo.write(carrera)

print("Archivo creado y guardado")