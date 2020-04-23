#Podemos abrir archivos en el disco duro con la instruccion "open"
#Para eso esta este modo, el cual consiste que en una variable la igualemos
#a un archivo que tengamos. Despues de eso para mostrarla se usa print(variable.read())

texto= open("PENNY.txt")

print(texto.read())

###Si tenemos el caso que nuestro archivo esta en una carpeta pero esa carpeta esta
##en el mismo directorio que nuestro archivo .py solo hacemos este comando: Ejemplo

texto= open("pancho/PENNY.txt")

print(texto.read())

##Otro caso es cuando nuestro archivo esta carpetas arriba de nuestro archivo de
##codigo, para eso se hace este modo: Ejemplo

texto= open("../pancho/PENNY.txt")

print(texto.read())
