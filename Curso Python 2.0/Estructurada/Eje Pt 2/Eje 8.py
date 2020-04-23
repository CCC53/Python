
def filtro():
    lista=[]
    opcion= input('Cuantas palabras desea añadir a la lista: ')
    opcion= int(opcion)
    for i in range(opcion):
        palabra= input('Escriba la palabra a añadir: ')
        lista.append(palabra)
    letra= input('Elije una letra: ')
    letra2= letra.upper()
    lista2=[]
    for i in range(len(lista)):
        new= list(lista[i])
        if new[0]== letra or new[0]== letra2:
            lista2.append(lista[i])
    for i in range(len(lista2)):
        print(lista2[i])

filtro()
