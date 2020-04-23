from random import randint

def partida():
    n=3
    puntos=0
    ganar=randint(0,1)
    while n>0:
        n-=1
        intento=int(input('Escriba un numero: '))
        if intento==ganar:
            puntos+=100
            print(f'Ha ganado, su puntaje es de {puntos}')
            ganar=randint(0,2)
            if n==0:
                print(f'Ha finalizado la partida con un puntaje de {puntos}')
                retry=input('¿Desea iniciar otra partida (s/n)?: ')
                if retry=='s':
                    partida()
                else:
                    print('Fin del juego')
        else:
            print(f'Su puntaje fue de {puntos}')
            ganar=randint(0,3)
            puntos=0
            if n==0:
                print(f'Ha finalizado la partida con {puntos}')
                retry=input('¿Desea volver a intentar (s/n?): ')
                if retry=='s':
                    partida()
                else:
                    print('Fin del juego')

partida()
