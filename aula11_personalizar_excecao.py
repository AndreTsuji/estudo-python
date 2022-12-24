from logging import exception


#Classe Error herda parametros de Exception
class Error(Exception):
    pass

#Classe InputError herda de Error
class InputError(Error):
    def __init__(self, message):
        self.message = message

#while true irá executar eternamente. O break finalizará o while, mas para isso o cod deve chegar lá sem erros.
while True:
    try:
        x = int(input("Entre com uma nota de 0 a 10: "))
        print (x)
        #Raise força uma exceção
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
            print('Valor inválido. Deve-se digitar apenas números.')
    except InputError as ex:
        print(ex)
