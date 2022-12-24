lista = [1, 3, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante']

# Verifica se existe elemento na lista
if 'lobo' in lista_animal:
    print('Existe lobo na lista_animal.')
else:  # append: adiciona elemento a lista
    print('Não existe lobo na lista_animal. Será adicionado')
    lista_animal.append('lobo')
    print(lista_animal)

# pop: remove elemento da lista. Se não tiver referência no () será removido o último valor.
lista_animal.pop(0)

# remove: remove elemento especifico da lista.
lista_animal.remove('elefante') 

# Sort: Ordena valores de forma crescente ou alfabetica
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)

# reverse: Ordena valores de forma decrescente ou alfabetica ao contrário
lista.reverse()
lista_animal.reverse()

#Converter lista em tupla e vice versa
tupla = tuple(lista)
lista = list(tupla)