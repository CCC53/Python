def inicio():
    print("\t\tBienvenido a su agenda telefonica")
    print("1.-Añadir contacto")
    print("2.-Mostrar contactos")

def escritura():
        nu= input("¿Cuantos contactos desea añadir?: ")
        num= int(nu)
        for i in range(0,num):
            agenda= open("../2/AGENDA_CHIDA.csv",'a')
            nombre= input("Escriba el nombre de contacto: ")
            telefono= input("Escriba el telefono de contacto: ")
            posicion= input("Escriba la posicion de contacto: ")
            agenda.write(posicion)
            agenda.write(",")
            agenda.write(nombre)
            agenda.write(",")
            agenda.write(telefono)
            agenda.write(",")
            agenda.write("\n")
            agenda.close()

def lectura(fin):
    agenda= open("../2/AGENDA_CHIDA.csv")
    for i in range (0,fin):
	    lec= agenda.readline()
	    print(lec.replace(",","\t\t"))
    agenda.close()
    print("Estos son todos sus contactos")

def nop():
	print("Esa opcion no existe")
