class Triangulo:
    def __init__(self):
        self.l1=int(input('Esciba el primero lado: '))
        self.l2=int(input('Esciba el segundo lado: '))
        self.l3=int(input('Esciba el tercer lado: '))
    def mayor(self):
        if self.l1>self.l2 and self.l1>self.l3:
            return f'El lado mayor es {self.l1}'
        elif self.l2>self.l1 and self.l2>self.l3:
            return f'El lado mayor es {self.l2}'
        else:
            return f'El lado mayor es {self.l3}'
    def tipo(self):
        if self.l1==self.l2 and self.l2==self.l3:
            return 'Es un triangulo equilatero'
        elif self.l1==self.l2 or self.l1==self.l3 or self.l2==self.l3:
            return 'Es un triangulo isoceles'
        else:
            return 'Es un triangulo escaleno'

triangulo1=Triangulo()
print(triangulo1.mayor())
print(triangulo1.tipo())

triangulo2=Triangulo()
print(triangulo2.mayor())
print(triangulo2.tipo())

triangulo3=Triangulo()
print(triangulo3.mayor())
print(triangulo3.tipo())
