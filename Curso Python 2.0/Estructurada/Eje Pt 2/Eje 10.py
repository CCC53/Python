
def bisiesto():
    año= input('Escriba un año cualquiera: ')
    año= int(año)
    if año%4==0 and año%100!=0:
        print('Es bisiesto')
    else:
        print('No es bisiesto')
        

bisiesto()
