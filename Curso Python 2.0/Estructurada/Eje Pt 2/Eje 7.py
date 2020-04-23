
edades= []
for i in range(0,10):
    edad= input('Escriba una edad: ')
    edad= int(edad)
    edades.append(edad)
    
for i in edades:
    if i <20:
        continue
    print(i)

print('Estas son las edades mayores o iguales a 20')


