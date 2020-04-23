#2

def funcion_mas_larga():
    lista=['Penny', 'Pancho', 'Maximo', 'Hatchi']
    if len(lista[0])>len(lista[1])and len(lista[0])>len(lista[2]) and len(lista[0])>len(lista[3]):
        print(lista[0])

    elif len(lista[1])>len(lista[0])and len(lista[1])>len(lista[2]) and len(lista[1])>len(lista[3]):
        print(lista[1])

    elif len(lista[2])>len(lista[0])and len(lista[2])>len(lista[1]) and len(lista[2])>len(lista[3]):
        print(lista[2])

    else:
        print(lista[3])

funcion_mas_larga()
