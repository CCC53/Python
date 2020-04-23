#Son usados para decidir hacer algo basado en que algo sea verdad o falsedad
x= 19
y=20
#Operadores para poder compaar: ==, !=, <, >, <=, >=

#If simple
if x>y:
    print(f"{x} es mayor que {y}")

#If/ else
if x>y:
    print(f"{x} es mayor que {y}")
else:
    print(f"{y} es mayor que {x}")

#elif
if x<y:
    print(f"{x} es menor que {y}")
elif x<=y:
    print(f"{x} es menor o igual que {y}")
else:
    print(f"{x} es mayor que {y}")

#if anidado
if x>10:
    if x<=y:
        print(f"{x} es mayor que 10 y menor o igual que {y}")

#Operaciones logicas: and, or y not= Usados para combinar las condiciones

#and
if x>10 and x<=y:
    print(f"{x} es mayor que 10 y menor o igual que {y}")

#or
if x>10 or x<=y:
    print(f"{x} es mayor que 10 o menor o igual que {y}")

#not
if not(x==y):
    print(f"{x} no es igual que {y}")

#Operadores de membresía (not, not in) - Los operadores de membresía se usan para probar si una secuencia se presenta en un objeto
#Son para hacer condiciones con una lista
numbers= [1,2,3,4,5]
X=3
Y=12
#In
if X in numbers:
    print(X in numbers)
#Not in
if Y not in numbers:
    print(Y not in numbers)

#Identify operators (is, is not) - Compara los objetos, no si son iguales, pero si en realidad son el mismo objeto, con la misma ubicación de memoria
n=3
m=4
#is
if n is m:
    print(n is m)
#is not
if n is not m:
    print(n is not m)



