def inicio():
    print("\t\tBienvenido a su agenda telefonica")
    print("1.-Añadir contacto")
    print("2.-Mostrar contactos")
    print("3.-Buscar un contacto en especial")

def escritura():
    nombre= input("Escriba el nombre de contacto: ")
    telefono= input("Escriba el telefono de contacto: ")
    agenda= open("../2/AGENDA_CHIDA.csv")
    for i in range(1,40):
        linea= agenda.readline()
        partida= linea.split(",")
        if partida[0] != "":
            memoria= partida[0]
    agenda.close()
    memo= int(memoria)
    posci= memo+1
    posicion= 0
    poste= str(posci)
    agenda= open("../2/AGENDA_CHIDA.csv",'a')
    agenda.write(poste)
    agenda.write(",")
    agenda.write(nombre)
    agenda.write(",")
    agenda.write(telefono)
    agenda.write(",")
    agenda.write("\n")
    agenda.close()

def lectura(ncon):
    agenda= open("../2/AGENDA_CHIDA.csv")
    for i in range (0,ncon):
	    lec= agenda.readline()
	    print(lec.replace(",","\t\t"))
    agenda.close()
    print("Estos son todos sus contactos")

def nop():
	print("Esa opcion no existe")

def buscar(buscador,numero):
    print("Aqui buscaré las coincidencias")
    agenda= open("../2/AGENDA_CHIDA.csv")
    for i in range(0,numero):
        lec= agenda.readline()
        partida= lec.split(',')
        if buscador== partida[1]:    
            print(partida)
    agenda.close()
