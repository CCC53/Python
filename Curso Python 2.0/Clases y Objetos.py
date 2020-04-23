#Una clase es como un plano para crear objetos. Un objeto tiene propiedades y métodos (funciones) asociados con él. Casi todo en Python es un objeto

#Crear clase
class User:
    #Constructor es básicamente una función que se ejecuta cuando crea una instancia de un objeto de una clase
    def __init__(self, name, email, age):
        self.name= name
        self.email= email
        self.age= age
    #Todo metodo debe tener en los parametros 'self'
    def saludo(self):
        return f'Mi nombre es {self.name} y tengo {self.age} años'
    def has_birthday(self):
        self.age= self.age+1
#Extender una clase
class Costumer(User):
    def __init__(self, name, email, age):
        self.name= name
        self.email= email
        self.age= age
        self.balance= 0
    def set_balance(self, balance):
        self.balance= balance
    def saludo(self):
        return f'Mi nombre es {self.name}, tengo {self.age} años y de balance {self.balance}'

#objetos de usuario de inicio
brad= User('Brad Pitt', 'bradpitt@gmail.com', 40)
brad.has_birthday()
print(brad.saludo())

#Inicializar costumer
Janet= Costumer('Janet Jackson', 'janette@yahoo.com', 38)
Janet.set_balance(500)
print(Janet.saludo())
