class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular=titular
        self.cantidad=cantidad
    def mostrar(self):
        return f'El titular de la cuenta es {self.titular} y cuenta con {self.cantidad} de saldo'

class Caja(Cuenta):
    def __init__(self, titular, cantidad):
        Cuenta.__init__(self, titular, cantidad)

class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, ):
        Cuenta.__init__(self, titular, cantidad)
        self.plazo=int(input('Escriba el plazo: '))
        self.interes=float(input('Escriba la taza de interes: '))
    def importe(self):
        self.importe=(self.cantidad*self.interes)/100
        return f'El importe de interes es de {self.importe}'
    def datos(self):
        return f'Su plazo en dias es: {self.plazo}\nSu interes es de: {self.interes}'
        
caja1=Caja('Penny', 7000)
print(caja1.mostrar())
plazo1=PlazoFijo('Penny', 7000)
print(plazo1.datos())
print(plazo1.importe())    
 
 
 

