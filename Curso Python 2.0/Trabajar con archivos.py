#Python tiene funciones para crear, leer, actualizar y eliminar archivos

#Abrir un archivo
myFile= open('myfile.txt', 'w')

#Conseguir informacion
print('Nombre: ', myFile.name)
print('Cerrado: ', myFile.closed)
print('Modo de apertura: ', myFile.mode)

#Escribir en el archivo
myFile.write('Estoy aprendiendo Python,')
myFile.write(' es un lenguaje chido')
myFile.close()

#Adjuntar al archivo
myFile= open('myfile.txt', 'a')
myFile.write('\nDespues inicio Django')
myFile.close()

#Leer un archivo
myFile= open('myfile.txt', 'r+')
texto= myFile.read()
print(texto)
