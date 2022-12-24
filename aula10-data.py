from datetime import date, time, datetime, timedelta

#https://docs.python.org/3/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    #Formantando para padrão brasileiro
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.date())
    #Retornando dia da semana em inglês e traduzida
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo', 'Domingo')
    print(tupla[data_atual.weekday()])
    #Criando data
    data_criada = datetime(2018,6,20,15,30,20)
    print(data_criada)
    #Convertendo string em data
    data_string = '10/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    #Adicionando ou subtraindo tempo a determinada data
    nova_data = data_convertida + timedelta(days=365, hours=2, minutes=15)
    print(nova_data)

def trabalhando_com_date():
    data_atual = date.today()
    #Formatando a data para formato brasileiro com ano em 4 digitos
    print(data_atual.strftime('%d/%m/%Y'))

def Trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))

trabalhando_com_datetime()