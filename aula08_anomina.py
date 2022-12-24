# Ex2 Comparação função normal e função anônima (lambda)-------------------------------
# def contador_letras(lista_palavras):
#         contador = []
#     for x in lista_palavras:
#         quantidade = len(x)
#         contador.append(quantidade)
#     return contador

def contador_letras(lista): return [len(x) for x in lista]
def soma(a, b): return a + b


lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

# Ex3 Criar um dicionador para agrupar funções lambda
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

div = calculadora['divisao']
print('A divisão é: {}.'.format(div(10, 5)))
