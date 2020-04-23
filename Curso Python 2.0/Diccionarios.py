#Diccionario: Es una colección desordenada, modificable e indexada. No hay miembros duplicados

#Crear un diccionario
personal= {
    "nombre": "Carlos",
    "apellido": "Calette",
    "edad": 18
    }
#Usando constructor
#personal2= dict(nombre= "Karen", apellido= "Martinez")
#print(personal2, type(personal2))

#Imprimir un dato especifico
print(personal["nombre"])
print(personal.get("apellido"))

#Añadir un dato nuevo
personal["phone"]= "55-9146-9572"
print(personal)

#Obtener las claves del diccionario
print(personal.keys())

#Obtener elementos del diccionario
print(personal.items())

#Copiar diccionario
personal2= personal.copy()
personal2["city"]= "CDMX"

print(personal2)

#Remover un elemento del diccionario
del (personal["edad"])
print(personal)
#
personal.pop("phone")
print(personal)

#Limpiar dic
personal.clear()
print(personal)

#Mostrar longitud del dic
print(len(personal2))

#Lista de dic
perros= [
    {"nombre": "Penny", "edad": 23},
    {"nombre": "Pancho", "edad": 70}
    ]

print(perros[0]["nombre"])















