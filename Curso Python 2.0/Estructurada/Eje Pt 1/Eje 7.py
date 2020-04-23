#7

def es_palindromo():
    cadena= input('Escriba una cadena: ')
    print(cadena,'\n') 
    inversora= cadena[::-1]
    print(inversora)
    if inversora== cadena:
        print('\nTrue')
    else:
        print('\nFalse')

es_palindromo()
