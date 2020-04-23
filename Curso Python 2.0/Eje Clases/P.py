class Usuario:
    def __init__(self, contra, nombre, foto):
        self.contra=contra
        self.nombre=nombre
        self.foto=foto
    def restablecer(self, newcontra):
        self.contra=newcontra
    def obtener(self):
        return self.nombre
    def obtecont(self):
        return self.contra

class Tarea:
    def __init__(self, nombre, fecha, descripcion):
        self.nombre=nombre
        self.fecha=fecha
        self.descripcion=descripcion
    def setnombre(self, nombre2):
        self.nombre=nombre2
    def setdate(self, fecha2):
        self.fecha= fecha2
    def setdescrip(self, descripcion2):
        self.descripcion=descripcion2
    def name(self):
        return self.nombre
    def date(self):
        return self.fecha
    def descrip(self):
        return self.descripcion

usuario1=Usuario('5273', 'Penny', 'Foto1.jpg')
print(usuario1.obtener())
print(usuario1.obtecont())
usuario1.restablecer('1234')
print(usuario1.obtecont())

usuario2=Usuario('5436', 'Fransisco', 'Foto2.jpg')
print(usuario2.obtener())
print(usuario2.obtecont())
usuario2.restablecer('7890')
print(usuario2.obtecont())

tarea1= Tarea('t1', '01/01/19', 'Nada')
print(tarea1.name())
tarea1.setnombre('tarea1')
print(tarea1.name())
print(tarea1.date())
tarea1.setdate('22/06/19')
print(tarea1.date())
print(tarea1.descrip())
tarea1.setdescrip('Fransisco ya es muy viejo')
print(tarea1.descrip())
