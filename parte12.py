contador_letras = lambda lista: [len(x) for x in lista]
lista_animais = ['cachorro']
print(contador_letras(lista_animais))
soma = lambda a,b: a + b
sub = lambda a, b: a - b
print (sub(-1,8))
print (soma(1,2))

calculadora = {
    'soma': lambda a, b: a + b,
    'sub' : lambda a, b: a - b,
    'mult': lambda a, b: a * b,
}
print(type(calculadora))
soma = calculadora['soma']
mult = calculadora ['mult']
print(soma(10,4))
print(mult(9,9))