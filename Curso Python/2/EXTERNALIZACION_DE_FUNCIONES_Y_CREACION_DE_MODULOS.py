####Para hacer nuestros programas mas eficientes y poder reutilizar funciones
##se hace el metodo de externalizarlas, es decir separarlas en otro archivo, el cual
##podemos mandar a llamar con la instruccion import el nomhre del archivo:

import FUNCIONES_EN_MODULOS

FUNCIONES_EN_MODULOS.inicio()
opcion= input("Elija una opcion: ")
print("Ha elegido la opcion",opcion)
if opcion == "1":
	FUNCIONES_EN_MODULOS.escritura()
	
elif opcion == "2":
	nco= input("¿Cuantos contactos desea leer?: ")
	ncon= int(nco)
	FUNCIONES_EN_MODULOS.lectura(ncon)
else:
	FUNCIONES_EN_MODULOS.nop()
