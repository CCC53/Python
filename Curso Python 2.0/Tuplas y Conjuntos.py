"""
Tuplas y Conjuntos

Una tupla es una colección que está ordenada y que no se puede ser alterada. Permite duplicar números.

Un conjunto es una colección que no está ordenada ni indexada. No hay números duplicados.
"""

#Tuplas

#Creacion de duplas
perros= ("Penny", "Pancho", "Hatchi")

#Si es dupla de un solo element se tiene que poner una coma al finl
perro= ("Pancho",)

#Con constructor y no es tan comun
#perros2= tuple(("Penny", "Pancho", "Hatchi"))
#print(perros, perros2)

#Conseguir un elemento especifico de una tupla
##print(perros[1])

#Manda error porque una tupla no se puede modificar
##perros[1]= "Maximo"
##print(perros[1])

#Eliminar una tupla
del perro

#Ver la longitud de la tupla
print(len(perros))

#Conjuntos
perros2= {"Penny", "Pancho", "Hatchi"}

#Checar si un elemento esta en el conjunto++
print("Pancho" in perros2)

#Añadir al conjunto
perros2.add("Maximo")
print(perros2)

#Remover elemento
perros2.remove("Maximo")
print(perros2)

#Limpiar conjunto
perros2.clear()
print(perros2)

#Borrar conjunto
del perros2
print(perros2)
