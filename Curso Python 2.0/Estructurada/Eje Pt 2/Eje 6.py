
def registro():
    año= input('Escriba el año en curso: ')
    año= int(año)
    for i in range(0,3):
        nombre= input('Escriba su nombre: ')
        año2= input('Escriba su año de nacimiento: ')
        año2= int(año2)
        cumple= año-año2
        print(f'Su nombre es {nombre}, su año de nacimiento es {año} y la edad que cumple en este año es {cumple}')

registro()
