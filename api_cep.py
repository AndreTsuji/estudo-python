import requests

lista_ceps = ['37068-002', '61608-050', '97500-300', '89107000', '99709-130', '06680-420', '74530240']
lista_enderecos = []

for cep in lista_ceps:
    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
    try:
        req = requests.get(url, timeout=None)
        if req.status_code == 200:
            # API acessada com sucesso.
            endereco = req.json()
            lista_enderecos.append(
                [
                    endereco['cep'],
                    #endereco['logradouro'],
                    endereco['localidade'],
                    endereco['uf']
                ]
            )
        else:
            erro = req.raise_for_status()
            print(f'Ocorreu o seguinte erro no acesso da API: {erro}')

    except Exception as erro:
        print(f'Ocorreu o seguinte erro na execução do código: {erro}')

for item in lista_enderecos:
    print(item)
