#En este programa se hara un ejemplo muy simple con el uso de entradas
print("\tSaludos")
nombre= input("Escriba su nombre: ")
print("El nombre que has digitado es: ",nombre)
#Por defecto python convierte las variables en tipo string y para convertirlo a entero o flotante se hace esto:
edad= input("Ahora escriba su edad: ")
#Primero se almacena en una variable e inmediatamente se convierte a entero o flotante pero
#se necesita otra variable donde se pueda almacenar el entero o flotante
edadnum= int(edad)
print("El triple de su edad es: %d"%(edadnum*3))
