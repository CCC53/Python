class Alumno:
    def __init__(self,nombre, calificacion):
        self.nombre=nombre
        self.calificacion=calificacion
    def mostrar(self):
        return f'El alumno {self.nombre} tiene de calificacion {self.calificacion}'
    def aprobar(self):
        if self.calificacion>=6:
            return f'El alumno {self.nombre} ha aprobado'
        else:
            return f'El alumno {self.nombre} esta reprobado' 
    
alumno1=Alumno('Carlos', 5)
print(alumno1.mostrar())
print(alumno1.aprobar())

alumno2=Alumno('Jair', 7)
print(alumno2.mostrar())
print(alumno2.aprobar())
