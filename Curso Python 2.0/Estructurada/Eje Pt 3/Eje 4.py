def tasa():
    c=int(input('Escriba el dinero en dolares: '))
    x=float(input('Escriba la tasa de interes: '))
    n=int(input('Escriba el plazo: '))
    C=c*(1+x/100)**n
    print(f'El capital inicial transcurridos esos años se convirtio en {C}')

tasa()
