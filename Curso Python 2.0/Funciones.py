"""
Una función es un bloque de código que solo se ejecuta cuando se llama.
En Python, no utilizamos corchetes, utilizamos sangría con tabulaciones o espacios
"""

#Creacin de funcion
def hola(nombre="Carlos"):
    print(f"Hola {nombre}")

hola()

def numero(n1,n2):
    suma=n1+n2
    return suma

n= numero(5,7)
print(n)

#Una función lambda es una pequeña función anónima

#Una función lambda puede tomar cualquier número o argumento, pero solo puede tener una expresión

numero= lambda n1, n2: n1+n2
print(numero(12,4))
