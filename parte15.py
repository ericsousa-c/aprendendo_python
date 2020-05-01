
lista = [3, 10]
try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 4/1
    lista[0]
    x = 4


except ZeroDivisionError:
    print('Não é possivel man')
except ArithmeticError:
    print('houve um erro ao realizar sua operacao')
except IndexError:
    print('Erro ao acessar um indice invalido')
except Exception as ex:
    print('erro desconhecido {}'.format(ex))
else:
    print('td mec')
finally:
    print('fechando')
    arquivo.close()
