name, age= ('Fransisco', 18)
#Concadenar un string y un int
print("Mi nombre es " +name +" y tengo " +str(age))

#Otra manera de juntar variables para hacer un cadena es por posicion
print("Mi nombre es {name} y tengo {age}".format(name=name, age=age))

#Otra manera es por el metodo F-string (de Python 3.6 en adelante)
print(f"Mi nombre es {name} y tengo {age}")

#Metodos de cadena
S= "hola mundo"
#Primer letra en mayuscula
print(S.capitalize())
#Todo en mayusculas
print(S.upper())
#Todo en minusculas
print(S.lower())
#Swap case
print(S.swapcase())
#Get Lenght
print(len(S))
#Replace
print(S.replace("mundo", "todos"))
#Count
sub= "h"
print(S.count(sub))
#Starts with
print(S.startswith("hola"))
#Ends with
print(S.endswith("o"))
#Split into a list
print(S.split())
#Find posistion
print(S.find("d"))
#Is all alphanumeric
print(S.isalnum())
#Is all alphabetic
print(S.isalpha())
#Is all numeric
print(S.isnumeric())
