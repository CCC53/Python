class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def mostrar(self):
        return f'La persona {self.nombre} tiene {self.edad} años de edad'
    def legal(self):
        if self.edad>=18:
            return f'{self.nombre} es mayor edad'
        else:
            return f'{self.nombre} aun es menor'

persona1=Persona('Carlos', 18)
print(persona1.mostrar())
print(persona1.legal())

persona2=Persona('Jair', 17)
print(persona2.mostrar())
print(persona2.legal())
