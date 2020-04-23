
def max_in_list():
    lista=[70,30,40,100,20,10,80,50]
    cont=lista[0]
    for k in lista:
        if k>cont:
            cont=k
            if k>=cont:
                print(f'El numero mayor es {cont}')

max_in_list()
        
