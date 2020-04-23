##class Perro:
##    def __init__(self, nombre, raza, edad):
##        self.nombre= nombre
##        self.raza= raza
##        self.edad= edad
##    def name(self):
##        return f'El nombre del perro es {self.nombre},'
##    def especie(self):
##        return f'es de la raza {self.raza}'
##    def age(self):
##        return f'y tiene {self.edad} años de edad'
##
##pancho= Perro('Pancho', 'labrador', 11)
##print(pancho.name(), pancho.especie(), pancho.age())
##
##penny= Perro('Penny', 'labradora', 6)
##print(penny.name(), penny.especie(), penny.age())
##
##hatchi= Perro('Hatchi', 'boxer', 4)
##print(hatchi.name(), hatchi.especie(), hatchi.age())

class Lapiz:
    def __init__(self, tipo, punta, goma):
        self.tipo=tipo
        self.punta= punta
        self.goma= goma
    def borrar(self):
        if self.goma== True:
            print('El lapiz puede borrar por tener goma integrada')
        else:
            print('El lapiz no puede borrar por si mismo')
        

lapiz= Lapiz('Dibujo', 'Fina', False)
lapiz.borrar()
