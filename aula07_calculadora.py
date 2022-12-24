# #Ex 1 funções -------------------------------
# from operator import truediv


# def soma (a, b):
#     return a + b

# def subtracao (a, b):
#     return a - b

# print(soma(1, 2))
# print(subtracao(10,2))

# Ex 2 utilizando classe-----------------------------------
class Calculadora:  # Por convensão classes começam com maiusculas e funções/métodos minusculos
    # caso queira que cada função na classe receba entradas diferentes, não usar a função init
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
        pass

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b


# Só executa trecho se for chamado pelo próprio módulo. Bom para trechos de teste.
if __name__ == '__main__':
    calc = Calculadora(10, 2)
    print(calc.valor_a)
    print(calc.valor_b)
    print(calc.soma())
    print(calc.subtracao())
