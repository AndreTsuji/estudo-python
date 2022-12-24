#Criando Exceções
#documentação de exceções padrões do python https://docs.python.org/3/library/exceptions.html
from logging import exception

try:
    diviao = 10 / 0
    numero = lista [1]

#Ao identificar o Erro será verificado na ordem do cod se o erro pertence a exceção
except ZeroDivisionError:
    print('Não é possivel realizar divisão por 0')
#As classe de exceções possuem a hierarquia pai>filho, podendo usar classes mais genericas ou mais espeficas.
except ArithmeticError:
    print('Houve um erro ao realizar uam operação aritimética')
except IndexError:
    print ('Erro ao acessar um índice inválido da lista')
except exception as ex:
    print('Erro desconhecido.Erro: {}'.format(ex))
#só executará o else se não der nenhum erro
else:
    print('Executa quando não ocorre exceção')
#Executa se der erro ou não. Tudo que tiver dentro do try e abaixo do erro não será executado
finally:
    print('Sempre executa')