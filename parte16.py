class Error(Exception):
    pass
class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('coloque um valor de 0 a 10'))
        print(x)
        if x>10 or x<0:
            raise InputError ('valor invalido coloque um valor de 0 a 10')
        break
    except ValueError:
        print('valor invalido apenas numeros')
    except InputError as ex:
        print(ex)
