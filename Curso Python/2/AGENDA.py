agenda= open("AGENDA2.0.csv",'a')

nombre= input("Escriba el nombre de contacto: ")
telefono= input("Escriba el numero de telefono: ")

print("Nombre de contacto:",nombre,"\nTelefono de contacto:",telefono)
print("Su contacto se ha guardado en la agenda")

agenda.write(nombre)
agenda.write(",")
agenda.write(telefono)
agenda.write("\n")

agenda.close()

##Exsisten tres metodos para abrir un archivo el cual viene por defecto y solo
##permite la operacion de lectura. El write que es 'w' que consiste en escritura
##pero tiene el incoveniente que se elimina el contenido cada vez que se guarda
##un nuevo dato. La ultima es el añadido o add el cual se pone 'a' de esta manera
##y este consiste en escribir un nuevo dato pero respetando el contenido anterior
##
