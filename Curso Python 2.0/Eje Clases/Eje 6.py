class Banco:
    def __init__(self):
        self.cliente1=cliente1
        self.cliente2=cliente2
        self.cliente3=cliente3
    def operaciones(self):
        print('\t\tCajero')
        print('1.Depositar\n2.Retirar')
        self.opcion=input('Elija una operacion: ')
        if self.opcion=='1':
            Cliente.deposito(self)
            print(Cliente.mostrar(self))
        else:
            Cliente.retiro(self)
            print(Cliente.mostrar2(self))
    def depo_total(self):
        self.total=cliente1.deposito()+cliente2.deposito()+cliente3.deposito()
        return f'El total del banco fue de {self.total}'
        
class Cliente(Banco):
    def __init__(self,nombre,cantidad):
        self.nombre=nombre
        self.cantidad=cantidad
    def deposito(self):
        self.cant=int(input('Escriba la cantidad a depositar: '))
        self.cantidad+=self.cant
    def retiro(self):
        self.cant2=int(input('Escriba la cantidad a retirar: '))
        self.cantidad-=self.cant2
    def mostrar(self):
        return f'Estimado usuario {self.nombre}\nHa depositado {self.cant}, su saldo es de {self.cantidad}'
    def mostrar2(self):
        return f'Estimado usuario {self.nombre}\nHa retirado {self.cant2}, su saldo es de {self.cantidad}'

cliente1=Cliente('Penny', 5000)
cliente1.operaciones()
cliente2=Cliente('Pancho', 7000)
cliente2.operaciones()
cliente3=Cliente('Hatchi', 30000)
cliente3.operaciones()
