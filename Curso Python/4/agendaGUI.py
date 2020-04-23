##En esta unidad se comienza con Tkinter que es la interfaz grafica y para llamarla
##o importar todos los elementos de esta libreria se hace: from tkinter import * que quiere
##decir que se importara todo el contenido de la libreria

from tkinter import *

import FUNCIONES_EN_MODULOS

def escribe():
    agenda= open("../2/AGENDA_CHIDA.csv")
    for i in range (0,11):
        lec= agenda.readline()
        lista.insert(END, lec.replace(",","  ") )
    agenda.close()
    


##Un frame es la ventana que va a contener nuestra aplicacion grafica
f= Frame(height=1000, width=1000, cursor="pirate")
f.pack(padx=15, pady=15)
##Aqui lo que se hace empaquetar nuestro frame y lanzarlo y ademas se hara padding
##que es el margen interior de los elementos contenidos en el frame

##Ademas de texto igual se añadiran imagenes:
photo= PhotoImage(file= "IMAGENES/unnamed (12).png", width=290, height=290)
imagen= Label(f, image=photo)
imagen.pack(side=TOP, padx=2, pady=2)

##Se mostrara un ejemplo de poner etiquetas y las propiedades o parametros como
##el tamaño de letra, color de fuente y tipo de fuente:
titulo= Label(f,text="Agenda Telefonica", fg="green", font=("Arial Narrow",21))
titulo.pack(side=TOP, padx=10, pady=10)
kreator= Label(f,text="Hecha por Carlos Calette")
kreator.pack(side=TOP, padx=10, pady=10)

##Se pueden añadir campos de texto que se pueden usar como entradas:
campo= Entry(f, textvariable= 0)
campo.pack(side=BOTTOM, padx=8, pady=10)

##Se hara el ejemplo de listar los contenidos de la agenda sustituyendo el parametro
##definido
##Para que al llamar la funcion NO HAY QUE PONER los parentesis, si se ponen se vera
##en la linea de comandos

##Al colocar el parametro se tiene que hacer Entry.get(nombre), pero haciendo esto se genera el error de str y el int
##lo que se puede hacer es crear una variable intermedia o hacer esto: int(Entry.get(nombre))

##Se pueden añadir botones que mas tarde se pueden enlazar a que realicen una accion ya
##definida
##Para que un boton realice una accion solo se indica la instruccion command y mandar a llamar
##a la funcion si no tiene parametros, si los tiene se tiene que usar la instruccion
##lambda que sirve para llamar a las funcione con parametros

##boton= Button(f,text="Listar sus contactos",command= lambda: FUNCIONES_EN_MODULOS.lectura(int(Entry.get(campo))))
boton= Button(f,text="Listar sus contactos",command=escribe)
boton.pack(side=BOTTOM, padx=5, pady=5)

##En este ejemplo se hara un campo de lista
lista= Listbox(f)
lista.pack(side=TOP,padx=10, pady=10)








