class Calculadora:


    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def sub(self, valor_a, valor_b):
        return valor_a - valor_b

    def div (self, valor_a, valor_b):
        return valor_a / valor_b

    def mult(self, valor_a, valor_b):
        return valor_a * valor_b


calculadora = Calculadora()
print(calculadora.soma(1, 2))
print(calculadora.sub(10, 5))
print(calculadora.div(10, 3))
print(calculadora.mult(10, 10))