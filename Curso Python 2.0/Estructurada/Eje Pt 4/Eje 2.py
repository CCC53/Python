def factura(codigo):
	if codigo==1:
		precio=250
		print(f'El precio es de ${precio}')
		unidad=int(input('Cuantas piezas va a comprar: '))
		compra= precio*unidad
		print(f'El total a pagar es de ${compra}')
		salida()
	elif codigo==2:
		precio=150
		print(f'El precio es de ${precio}')
		unidad=int(input('Cuantas piezas va a comprar: '))
		compra= precio*unidad
		print(f'El total a pagar es de ${compra}')
		salida()
	elif codigo==3:
		precio=300
		print(f'El precio es de ${precio}')
		unidad=int(input('Cuantas piezas va a comprar: '))
		compra= precio*unidad
		print(f'El total a pagar es de ${compra}')
		salida()
	elif codigo==4:
		precio=20
		print(f'El precio es de ${precio}')
		unidad=int(input('Cuantas piezas va a comprar: '))
		compra= precio*unidad
		print(f'El total a pagar es de ${compra}')
		salida()
	elif codigo==5:
		precio=400
		print(f'El precio es de ${precio}')
		unidad=int(input('Cuantas piezas va a comprar: '))
		compra= precio*unidad
		print(f'El total a pagar es de ${compra}')
		salida()
	else:
		precio=150
		print(f'El precio es de ${precio}')
		unidad=int(input('Cuantas piezas va a comprar: '))
		compra= precio*unidad
		print(f'El total a pagar es de ${compra}')
		salida()

def tabla():
	print('Tabla de Productos:\n')
	print('Producto\t\tCodigo')
	print('Camisa....................1')
	print('Cinturon..................2')
	print('Pantalon..................3')
	print('Calcetines................4')
	print('Sueter....................5')
	print('Corbata...................6')

def salida():
	opcion=input('Presione 1 para salir o 2 para hacer otra compra: ')
	if opcion=='1':
		print('Vuelva pronto')
	elif opcion=='2':
		tabla()
		codigo=int(input('\nIntroduza codigo de producto: '))
		factura(codigo)
	else:
		print('Esa opcion no existe')
		salida()

tabla()
codigo=int(input('\nIntroduza codigo de producto: '))
factura(codigo)
