# #Ex1: Verifica se valor digitado é primo ---------------------------------------
# a = int(input('Entre com um número: '))

# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     if resto == 0:
#         div += 1

# if div <= 2:
#     print('Número {} é primo.'.format(a))
# else:
#     print('Número {} não é primo.'.format(a))

# # Ex2: Quais valores são primos ---------------------------------------
# a = int(input('Entre com um número: '))
# for num in range(1, a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)

# Ex3 calculo de média de notas -----------------------------------------------------------------
a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))

media = (a + b + c + d) / 4
print('Média: {}.'.format(media))