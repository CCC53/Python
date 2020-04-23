import re

def validamail(email):
    if len(email)>7:
        return bool(re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', email)
        )
