#2

def max_de_tres(n1,n2,n3):
    if n1>n2 and n1>n3:
        print(n1)
    elif n2>n1 and n2>n3:
        print(n2)
    else:
        print(n3)

n1= input("Escriba un numero: ")
n1= int(n1)
n2= input("Escriba otro numero: ")
n2= int(n2)
n3= input("Escriba un ultimo numero: ")
n3= int(n3)
max_de_tres(n1,n2,n3)
