a = int(input('nota1'))
while a > 10:
    a = int(input('tem parada errada'))

b = int(input('nota2'))
while b > 10:
    b = int(input('tem parada errada'))

c = int(input('nota3'))
while c > 10:
    c = int(input('tem parada errada'))

d = int(input('nota4'))
while d > 10:
    d = int(input('tem parada errada'))

media = (a + b + c + d) / 4

print('media: {}'.format(media))


if media >=5:
    print('o aluno passo')
else:
    print('o aluno nao passo')

# a = int(input('botai'))
# b = int(input('again'))
#
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b == 0:
#     print('digitaro par')
# else:
#     print('no digitaro par')



# a = int(input('n1'))
# b = int(input('n2'))
# c = int(input('n3'))
# if a > b and a > c:
#     print('o numero maior é {}' .format(a))
# elif b > a and b > c:
#     print('o numero maior é {}' .format(b))
# else:
#     print ('o maior numero é {}'.format(c))
