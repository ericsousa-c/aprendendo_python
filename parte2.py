a = int(input('1º valor:'))
b = int(input('2º valor:'))
soma = a + b
sub = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print ('soma {soma} \nsub {sub}\ndivisao {divisao}\nmultiplicacao {multiplicacao}\nresto {resto}' .format(soma=soma, sub=sub, divisao=divisao, multiplicacao=multiplicacao, resto=resto))
