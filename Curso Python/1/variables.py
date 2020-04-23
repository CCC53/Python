#Para declarar variables solo hay que colocar el nombre e igualarla a algo, ejemplo
edad= 17
nombre= "Carlos"
apellido= "Calette"
#Como en todo lenguaje de programacion una variable no puede inicar su nombre
#con un numero. En python no es necesario colocar que tipo de variable es
#el lenguaje lo hace en automatico

print("Mi nombre es")
print(nombre)
print("y tengo")
print(edad)
print("años")
#Esta es una manera de usar texto e imprimir las variables pero son muchas lineas
#Se puede hacer en una sola linea uniendo todo con comas, ejemplo

#Si queremos hacer operaciones con variables es recomendable hacer la operacion entre
#parentesis. Ejemplo
print("Mi nombre es",nombre,"y tengo",edad,"años y el doble de mi edad es",(edad*2),"años")

##Otra manera de encadenar codigo es la siguiente, se puede usar la anterior pero
##muchos se les hace mas comoda esta manera
print("Mi nombre completo es: %s %s y tengo %f años y la mitad de mi edad es %.2f"%(nombre, apellido, edad, (edad/2)))
##Esta manera consiste en mandar a llamar la variable por su tipo y despues
##al terminar la cadena de texto mandar a llamar a las variables por su nombre y en
##el orden correcto de esta manera %(variable, variable2), esto va afuera de la cadena

