def contador_palavras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador
def teste():
    return 'teste'
if __name__ == '__main__':
    lista = ['cachorrorytyrty', 'gato']
    print(contador_palavras(lista))

