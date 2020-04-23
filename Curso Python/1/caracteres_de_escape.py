##Un caracter de escape sirve para poder usar al mismo tiempo las comillas dobles o las
##sencilas, no todos sirven para eso para esta situacion se utiliza solo "\". Ejemplo

print("En una leccion pasada dije que mi nombre era \"Carlos\"")
print('Y en la leccion pasada dije que mi apellido era \'Calette\'')

##Anteriormente hemos separado lineas pero usando mas de un comando "print" pero
##podemos hacerlo con otro caracter de escape el cual es "\n" y "\r"
##La unica consideracion es que ambos caracteres sirven para lo mismo, solo que
##en desarrollo web el "\n" es mas familiarizado con los sistemas UNIX. LINUX Y MACOS10
##y el "\r" es mas comun en Windows. Ejemplo

print("Esta es una linea")
print("y esta es otra linea")
#Usando \n
print("Aquella es una linea \ny aquella es otra linea")
#Usando \r
print("Una linea \n \rotra linea")

##Otro caracter de escape es "\t" que es una forma muy basica de hacer tablas,
##este caracter sirve como el tabulador de nuestro teclado. Ejemplo
print("Nombre \t\tEdad\t\t Poblacion")
print("Juan \t\t41\t\t Atenco")
print("Juan Carlos \t17\t\t Ixtapan")
print("Javier \t\t22\t\t Nexquipayac")
