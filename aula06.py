# Ex1 criar conjuntos --------------------------------------------
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

# add: adiciona valor no conjunto
conjunto1.add(6)
print('Conjunto1 adicionando valor: {}'.format(conjunto1))
# dicard: remove valor do conjunto
conjunto1.discard(6)
print('Conjunto1 removendo valor: {}'.format(conjunto1))
# union: Novo conjunto com todos valores de 2 conjuntos
conjunto_uniao = conjunto1.union(conjunto2)
print('União conjuntos 1 e 2: {}'.format(conjunto_uniao))
# intersection: Novo conjunto com valores em comum de 2 conjuntos
conjunto_interseccao = conjunto1.intersection(conjunto2)
print('Intersecção conjuntos 1 e 2: {}'.format(conjunto_interseccao))
# difference: Novo conjunto com valores de um conjunto que não estão no outro
conjunto_diferenca1 = conjunto1.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto1)
print('Valores apenas no conjunto 1: {}'.format(conjunto_diferenca1))
print('Valores apenas no conjunto 2: {}'.format(conjunto_diferenca2))
# symmetric_difference: União de dois conjuntos sem valores em comum (oposto de Intersection)
conjuto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Valores apenas no conjunto 1: {}'.format(conjunto_diferenca1))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
# issubset: bolleano que retorna se um conjunto está contido em outro;
subset = conjunto_a.issubset(conjunto_b)
# issuperset: bolleano que retorna se um conjunto contém outro;
subset = conjunto_b.issubset(conjunto_a)

lista = ['gato', 'cachorro', 'elefante', 'elefante', 'lobo', 'gato']
# converter lista em conjunto e vice-versa. converter lista em conjunto remove duplicatas.
conjunto = set(lista)
lista = list(conjunto)
