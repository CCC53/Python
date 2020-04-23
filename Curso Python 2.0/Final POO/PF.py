from math import sqrt
from math import pi

class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f'({self.x},{self.y})'
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def getdistancia(self, puntoAux):
        return round((sqrt((puntoAux.getx()-self.x)**2+(puntoAux.gety()-self.y)**2)),2)

class Figura:
    def __init__(self,nombre,list1):
        self.nombre=nombre
        self.list1=list1
    
class Circulo(Figura):
    def __init__(self,nombre,list1):
        Figura.__init__(self,nombre,list1)
    def __str__(self):
        return f'La figura es un {self.nombre}'
    def getarea(self):
        r=list1[0].getdistancia(list1[1])
        return f'El area es de {round((pi*(r**2)),2)}'
    def getperimetro(self):
        r=list1[0].getdistancia(list1[1])
        return f'El perimetro es de {round((2*pi*r),2)}'

class Triangulo(Figura):
    def __init__(self,nombre,list1):
        Figura.__init__(self,nombre,list1)
    def __str__(self):
        return f'La figura es {self.nombre}'
    def tipo(self):
        r1=list1[0].getdistancia(list1[1])
        r2=list1[1].getdistancia(list1[2])
        r3=list1[0].getdistancia(list1[2])
        print (f'{r1} - {r2} - {r3}')
        if r1==r2 and r1==r3 and r3==r2:
            return 'Es un triangulo equilatero'
        elif r1!=r2 and r1!=r3 and r3!=r2:
            return 'Es un triangulo escaleno'
        else:
            return 'Es un triangulo isoceles'
    def getarea(self):
        r1=list1[0].getdistancia(list1[1])
        r2=list1[1].getdistancia(list1[2])
        return f'El area es de {(r1*r2)/2}'
    def getperimetro(self):
        r1=list1[0].getdistancia(list1[1])
        r2=list1[1].getdistancia(list1[2])
        r3=list1[0].getdistancia(list1[2])
        return f'El perimetro es de {r1+r2+r3}'

class Rectangulo(Figura):
    def __init__(self,nombre,list1):
        Figura.__init__(self,nombre,list1)
    def __str__(self):
        return f'La figura es {self.nombre}'
    def is_cuadrado(self):
        r1=list1[0].getdistancia(list1[1])
        r2=list1[0].getdistancia(list1[2])
        r3=list1[3].getdistancia(list1[2])
        r4=list1[1].getdistancia(list1[3])
        if r1==r2 and r1==r3 and r1==r4:
            return True
        else:
            return False
    def getarea(self):
        r1=list1[0].getdistancia(list1[1])
        r2=list1[0].getdistancia(list1[2])
        return f'El area es {r1*r2}'
    def getperimetro(self):
        r1=list1[0].getdistancia(list1[1])
        r2=list1[0].getdistancia(list1[2])
        return f'El perimetro es {(2*r1)+(2*r2)}'

punto1=Punto(-6,12)
punto2=Punto(-2,12)
punto3=Punto(-4,15.46)
punto4=Punto(7,8)
list1=[]
list1.append(punto1)
list1.append(punto2)
list1.append(punto3)
list1.append(punto4)

figura1=Circulo('Circulo', list1)
print(figura1)
print(figura1.getarea())
print(figura1.getperimetro())

figura2=Triangulo('Triangulo', list1)
print(figura2)
print(figura2.tipo())
print(figura2.getarea())
print(figura2.getperimetro())

figura3=Rectangulo('Rectangulo', list1)
print(figura3)
print(figura3.is_cuadrado())
print(figura3.getarea())
print(figura3.getperimetro())


