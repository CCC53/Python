ganar=['2','4','3','1']

n=4
while n>0:
    n-=1
    cadena=input('Cadena: ')
    cad=list(cadena)
    for i in range(len(cad)):
        for k in range(len(ganar)):
            if cad[i]==ganar[k] and i==k:
                print(True)
            elif cad[i]==ganar[k] or i==k:
                print('Almost')
            else:
                print(False)
