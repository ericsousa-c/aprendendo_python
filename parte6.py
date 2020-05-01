conjunto = {1,3,4,7}
conjunto2 = {10,1,3,2,2}
print(conjunto2)
conjunto_uniao = conjunto.union(conjunto2)
print('uniao: {}'.format(conjunto_uniao))
conjunto_inter = conjunto.intersection(conjunto2)
print('intersecção: {}'.format(conjunto_inter))
conjunto_diferenca = conjunto.difference(conjunto2)
print('diferença do 1 pro 2: {}'.format(conjunto_diferenca))
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('diferença do 2 pro 1: {}'.format(conjunto_diferenca2))
conjunto_diferenca_simetrica = conjunto.symmetric_difference(conjunto2)
print('diferença simétrica: {}'.format(conjunto_diferenca_simetrica))
conjunto_a = {1,2,3,4,4,5}
conjunto_b = {1,2,3,4,5,6,7,8,9,10}
conjunto_sub = conjunto_a.issubset(conjunto_b)
print('conjunto a é sub de b? {}'.format(conjunto_sub))
conjunto_super = conjunto_a.issuperset(conjunto_b)
print('conjunto a é super de b? {}'.format(conjunto_super))
animais = ['cachorro','cachorro','cachorro','gato', 'gato', 'macaco']
listanimais = set(animais)
print(animais, listanimais)

# conjunto = {1, 2, 3, 4}
# conjunto.add(5)
# print(conjunto)