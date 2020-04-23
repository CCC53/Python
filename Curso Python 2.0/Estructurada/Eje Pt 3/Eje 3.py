def riman(pal0,pal2):
    pal1=pal0[-2:]
    pal3=pal2[-2:]
    if pal1==pal3:
        print('Riman')
    else:
        print('No riman')

pal0=input('Escriba una palabra: ')
pal2=input('Escriba otra palabra: ')
riman(pal0,pal2)
