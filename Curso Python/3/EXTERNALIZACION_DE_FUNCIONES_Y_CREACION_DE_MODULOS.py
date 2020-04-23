####Para hacer nuestros programas mas eficientes y poder reutilizar funciones
##se hace el metodo de externalizarlas, es decir separarlas en otro archivo, el cual
##podemos mandar a llamar con la instruccion import el nomhre del archivo:

import FUNCIONES_EN_MODULOS


def principal():
        FUNCIONES_EN_MODULOS.inicio()
        opcion= input("Elija una opcion: ")
        print("Ha elegido la opcion",opcion)
        if opcion == "1":
                FUNCIONES_EN_MODULOS.escritura()
                principal()
        elif opcion == "2":
                nco= input("¿Cuantos contactos desea leer?: ")
                ncon= int(nco)
                FUNCIONES_EN_MODULOS.lectura(ncon)
                principal()
        elif opcion == "3":
                num= input("¿Cuantos contactos ha guardado?: ")
                numero= int(num)
                buscador= input("¿Que contacto desea buscar?: ")
                FUNCIONES_EN_MODULOS.buscar(buscador,numero)
                principal()
        else:
                FUNCIONES_EN_MODULOS.nop()
                principal()

principal()
