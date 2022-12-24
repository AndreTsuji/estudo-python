# # Ex1--------------------------------------------------------------
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
# if a > b and a > c:
#     print('O maior valor é {}'. format(a))
# elif b > c:
#     print('O maior valor é {}'.format(b))
# else:
#     print('O maior valor é {}'.format(c))
# print('Fim do programa')

# #Ex2-----------------------------------------------------------------
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b != 0:
#     print('Foi digitado um número par.')
# else:
#     print('Foi digitado um número impar.')

# Ex3 calculo de média de notas -----------------------------------------------------------------
a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))

media = (a + b + c + d) / 4
print('Média: {}.'.format(media))
