#Un bucle for se usa para iterar sobre una secuencia (es decir, una lista, una tupla, un diccionario, un conjunto o una cadena)

perros= ["Penny", "Pancho", "Cesar", "Hatchi"]

#Bucle for simple
"""
for perro in perros:
    print(f"Perro actual: {perro}")
"""
#Break (parar)
"""
for perro in perros:
    if perro== "Cesar":
        break
    print(f"Perro actual: {perro}")
"""
#Continuar e bucle
"""
for perro in perros:
    if perro== "Cesar":
        continue
    print(f"Perro actual: {perro}")
"""
#Range
'''
for i in range(len(perros)):
    print(perros[i])

for i in range(0,11):
    print(i)
'''
#Un bucle while ejecuta un conjunto de sentencias siempre que una condición sea verdadera
n=0
while n<=10:
    print(n)
    n=n+1
