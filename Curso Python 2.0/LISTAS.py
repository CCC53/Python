#Una lista es una colección que está ordenada y cambiable. Permite duplicar números

#Crear una lista
numbers= [1, 2 ,3, 4, 5]
perros= ["Penny", "Pancho", "Hatchi", "Maximo"]

"""
Usando un constructor
Esta es una manera no muy comun para crear listas
numbers2= list[(1, 2, 3, 4, 5)]

print(numbers, numbers2)
"""

#Conseguir un valor especifico de una lista, la base de una lista comienza en 0
print(perros[2])

#Obtener la longitud de una lista
print(len(perros))

#Añadir a la lista
perros.append("Cesar")
print(perros)

#Remover de la lista
perros.remove("Maximo")
print(perros)

#Insertar un elemento en una posición dada
perros.insert(2, "Obama")
print(perros)

#Quitar un elemento de una cierta posición
perros.pop(2)
print(perros)

#Revertir la lista (el ultimo elemento pasa a ser el primero y el primero el ultimo)
perros.reverse()
print(perros)

#Ordenar alfabeticamente
perros.sort()
print(perros)

#Invertir el orden alfabetico
perros.sort(reverse=True)
print(perros)
