##Aqui se hara la lectura del contenido de nuestra agenda como siempre se ha hecho
##hasta el momento
agenda= open("AGENDA2.0.csv")
##print(agenda.read())

##Aqui nuestros datos los lee todo como una sola cadena, pero si queremos mas control
##en la lectura se ocupa este formato: "variable.readline". Este es util para poder
##leer linea por linea de nuestros archivos

##Para hacer mas eficientes nuestros programas se usan estructuras de control
##y en este caso se veran las ciclicas comenzando por for
##para usar esto se hace asi:

##for i in range(0,4):
##    print(agenda.readline())
##print("Estos son todos sus contactos guardados")

##En este bucle se se ve claramente que todo lo que tenga sangria se incluira en
##el bucle
##Aqui se vera el bucle while que es muy similar al for pero solo que for si tiene
##conocimiento de donde inicia y donde termina. En while no tenemos la condicion de
##cierre de bucle. Ejemplo

n= 0
while n<24:
    print(agenda.readline())
    n= n + 1
print("Estos son todos sus contactos guardados")    
