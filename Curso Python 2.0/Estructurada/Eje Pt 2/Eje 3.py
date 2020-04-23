
def filtro():
    n= input('Cuantos caracteres desea tomar de referencia ')
    n= int(n)
    opcion= input('Cuantas palabras desea añadir: ')
    opcion= int(opcion)
    lista=[]
    for i in range(opcion):
        palabra= input('Escriba su palabra: ')
        lista.append(palabra)
    lista2=[]
    for i in range(len(lista)):
        if len(lista[i])>=n:
            lista2.append(lista[i])
    for i in range(len(lista2)):
        print(lista2[i])

filtro()
