from random import randint

def salida():
	opcion=input('Para salir presione 1 para salir o 2 para realizar otra compra: ')
	if opcion== '1':
		print('Vuelva pronto')
	else:
		dinero=int(input('Escriba la cantidad total de la compra: '))
		descuento(dinero)

def tabla():
    print('Color\t\t\tDescuento')
    print('Bola Blanca\t\tNo tiene')
    print('Bola Roja\t\t10% de descuento')
    print('Bola Azul\t\t20% de descuento')
    print('Bola Verde\t\t25% de descuento')
    print('Bola Amarilla\t\t50% de descuento')

def operacion(dinero):
	numero=randint(1,5)
	if numero==1:
		print('Usted saco una bola blanca, no recibe ningun descueto')
		print(f'Su total a pagar sigue siendo de ${dinero}')
	elif numero==2:
		print('Usted saco una bola roja, ha ganado un descuento del 10%')
		descuento=(10*dinero)/100
		precio=dinero-descuento
		print(f'Su nuevo total a pagar es de ${precio}')
	elif numero==3:
		print('Usted saco una bola azul, ha ganado un descuento del 20%')
		descuento=(20*dinero)/100
		precio=dinero-descuento
		print(f'Su nuevo total a pagar es de ${precio}')
	elif numero==4:
		print('Usted saco una bola verde, ha ganado un descuento del 25%')
		descuento=(25*dinero)/100
		precio=dinero-descuento
		print(f'Su nuevo total a pagar es de ${precio}')
	else:
		print('Usted saco una bola amarilla, ha ganado un descuento del 50%')
		descuento=(50*dinero)/100
		precio=dinero-descuento
		print(f'Su nuevo total a pagar es de ${precio}')

def descuento(dinero):
	referencia=3000
	if dinero>=referencia:
	    print(f'Su compra es de ${dinero} iguala o supera los ${referencia} y entrara en una promocion')
	    tabla()
	    operacion(dinero)
	    salida()
	else:
	    print(f'Su compra es de ${dinero}, no iguala o supera los ${referencia}')
	    salida()

dinero=int(input('Escriba la cantidad total de la compra: '))
descuento(dinero)
