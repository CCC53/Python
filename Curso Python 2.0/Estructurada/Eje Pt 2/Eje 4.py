import string

def contador():
    letras= string.ascii_uppercase
    letras= list(letras)
    mayusculas=[]
    palabra= input('Escriba una palabra: ')
    palabra=list(palabra)
    for i in range(len(palabra)):
        if palabra[i] in letras:
            mayusculas.append(palabra[i])
    print(f'La palabra tiene {len(mayusculas)} letra(s) mayuscula(s)')

contador()
