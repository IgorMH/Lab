import re
from datetime import datetime
from os import system

def validar_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]{2, 3}$'
    if re.search(regex, email):
        return True
    else:
        print('Formato de email invalido. Tente novamente.')
        return False

def validar_data(data):
    try:
        datetime.strptime(data, '%Y-%m-%d')
        return True
    except ValueError:
        print('Data invalida. Digite novamente.')
        return False