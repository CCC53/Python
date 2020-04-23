agenda= open("AGENDA.txt",'w')

##print(agenda.read())

##Para escribir en documentos que se abran en python se tiene que especificar
##que se va a escribir en el se tiene que usar "open("documento.xxx",'w')
##Para este caso, primero se eliminara el contenido que esta en el archivo con
##"variable.truncate" pero no es totalmente necesario

agenda.truncate()

agenda.write("En esta prueba se demuestra que se puede modificar archivos")

agenda.close()

