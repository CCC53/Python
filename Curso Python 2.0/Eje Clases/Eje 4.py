class calculadora:
    def __init__(self):
        self.n1=int(input('Escriba un numero: '))
        self.n2=int(input('Escriba otro numero: '))
    def mostrar(self):
        return f'El primero digito es {self.n1}\nEl segundo digito es {self.n2}'
    def operaciones(self):
        suma=self.n1+self.n2
        resta=self.n1-self.n2
        multi=self.n1*self.n2
        div=self.n1/self.n2
        return f'La suma es de {suma}\nLa resta es de {resta}\nEl producto es de {multi}\nEl cociente es de {div}'
        
ops=calculadora()
print(ops.mostrar())
print(ops.operaciones())
