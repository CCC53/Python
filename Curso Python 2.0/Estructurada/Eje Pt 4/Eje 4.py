def tabla():
	print('Categoria\t\tPrecio\t\tCodigo\t\tCouta por dia de atraso')
	print('Favoritos\t\t$20\t\t1\t\t\t$7')
	print('Nuevos\t\t\t$25\t\t2\t\t\t$8')
	print('Estrenos\t\t$30\t\t3\t\t\t$9')
	print('Superestrenos\t\t$40\t\t4\t\t\t$10')
def sistema():
	tabla()
	cat=input('\nDigite el codigo de la pelicula que rento: ')
	if cat=='1':
		couta=7
		dias=int(input('Digite los dias de retraso despues de la fecha de entrega: '))
		couta2=dias*couta
		print(f'El total a pagar por {dias} dias de retraso es de ${couta2}')
		operacion()
	elif cat=='2':
		couta=8
		dias=int(input('Digite los dias de retraso despues de la fecha de entrega: '))
		couta2=dias*couta
		print(f'El total a pagar por {dias} dias de retraso es de ${couta2}')
		operacion()
	elif cat=='3':
		couta=9
		dias=int(input('Digite los dias de retraso despues de la fecha de entrega: '))
		couta2=dias*couta
		print(f'El total a pagar por {dias} dias de retraso es de ${couta2}')
		operacion()
	else:
		couta=10
		dias=int(input('Digite los dias de retraso despues de la fecha de entrega: '))
		couta2=dias*couta
		print(f'El total a pagar por {dias} dias de retraso es de ${couta2}')
		operacion()
def operacion():
	op=input('Presione 1 para finalizar la operacion: ')
	if op=='1':
		print('El pago se ha realizado correctamente\n')
		tabla()
		sistema()
sistema()
