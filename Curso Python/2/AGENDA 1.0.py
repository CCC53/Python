##En este programa se hará una estructura de control para la agenda y tener todo
##en un solo codigo la lectura y escritura de datos

print("\tBienvenido a su Agenda Telefonica")
print("Opciones: \n1)Añadir un contactor \n2)Mostrar sus contactos")
opcion= input("Elija una opcion: ")
if opcion== "1":
        print("Ha elegido añadir un contacto a su agenda")
        opcion1= input("Numero de contactos a guardar: ")
        opcion2= int(opcion1)
        n=0
        while n<opcion2:
            agenda= open("AGENDA_CHIDA.csv",'a')
            nombre= input("Escriba el nombre de contacto: ")
            telefono= input("Escriba el numero de telefono: ")
            posicion= input("Escriba la posicion de contacto: ")
            print("Nombre de contacto:",nombre,"\nTelefono de contacto:",telefono)
            print("Su contacto se ha guardado en la agenda")
            agenda.write(posicion)
            agenda.write(",")
            agenda.write(nombre)
            agenda.write(",")
            agenda.write(telefono)
            agenda.write("\n")
            n= n+1
            agenda.close()
elif opcion== "2":
        print("Ha elegido mostrar sus contactos de agenda")
        opcion3= input("Numero de contactos que ha guardado: ")
        opcion4= int(opcion3)
        agenda= open("AGENDA_CHIDA.csv")
        n=0
        while n<opcion4:
            lectura= agenda.readline()    
            print(lectura.replace(",","\t\t"))
            n= n+1    
        agenda.close()
else:
        print("Esa opcion no es valida")

##Una manera de quitar las comas al imprimir los datos en pantalla se puede ahcer
##metiendo la instruccion de leer nuestro archivo en una variable y despues a
##esa variable se va al print con la instruccion de .replace() la cual debe tener
##dos parametros: el caracter que se quiere reemplazar y en una coma y comillas
##se coloca los caracteres nuevos a imprimir ejemplo: variable.replace("oldchar","newchar") 
