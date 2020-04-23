"""
Un módulo es básicamente un archivo que contiene un conjunto de funciones para incluir en sus aplicaciones.
Hay módulos básicos de python, los módulos se pueden instalar utilizando el administrador de paquetes pip (incluido Django), así como módulos personalizados
"""

import MODULOS2
from MODULOS2 import validamail

import datetime
from datetime import date
import time
from time import time
#today= datetime.date.today()
today= date.today()
hora= time()
print(today)
print(hora)

email= 'test@test.com'
if validamail(email):
    print("Correo valido")
else:
    print("Correo no valido")
