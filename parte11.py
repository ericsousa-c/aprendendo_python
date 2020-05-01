from funcao3 import Televisao
from funcao import Calculadora
from cont_pal import contador_palavras, teste

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
calculadora = Calculadora(5,10)
print(calculadora.mult())
lista = ['cachorro', 'gato', 'elefante']
print(contador_palavras(lista))
print(teste())
