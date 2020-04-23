#JSON se utiliza comúnmente con datos APIS. Aquí cómo podemos analizar JSON en un diccionario de Python

import json

#muestra
userJSON= '{"Nombre": "Janet", "Apellido": "Jackson", "Edad": 40}'

#parse
user= json.loads(userJSON)

print(user)
print(user["Nombre"])

#Operacion opuesta, de diccionario a JSON
car= {'Marca': 'Ford', 'Modelo': 'Mustang', 'Year': 1970}

carJSON= json.dumps(car)

print(carJSON)
