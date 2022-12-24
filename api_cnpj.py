import requests
import json
import time
import pandas

def importar_csv(endereco):
    tabela = pandas.read_excel(endereco)
    total_cnpj = []
    for linha in tabela['cnpj']:
        total_cnpj.append(str(linha).rjust(14, '0'))
    return total_cnpj

def cria_arquivo(endereco):
    # Criar um arquivo
    arquivo = open(endereco, 'w')
    #arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(endereco, lista):
    arquivo = open(endereco, 'a')
    for i in range(len(lista)):
        valor = lista[i]
        arquivo.write(valor + ',')
    arquivo.write('\n')
    #print(lista)
    arquivo.close()

def ler_arquivo(endereco):
    arquivo = open(endereco, 'r')
    texto = arquivo.read()
    print(texto)

#Consulta limitada a 3 CNPJs por minuto
#https://www.sintegraws.com.br/api/documentacao-api-receita-federal.php
def api_cnpj(lista_cnpj, loop):
    lista_dados = []
    for cnpj in lista_cnpj:
        url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
        querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}
        try:
            consulta = requests.request("GET", url, params=querystring)
            dado = json.loads(consulta.text)
            # API acessada com sucesso.
            ativ1 = dado['atividade_principal']
            cnae_cod1 = ativ1[0]['code'].replace(",",";")
            cnae_text1 = ativ1[0]['text'].replace(",",";")
            cont = 0
            ativ2 = dado['atividades_secundarias']
            while cont < len(ativ2):
                if cont == 0:
                    cnae_cod2 = ativ2[cont]['code'].replace(",",";")
                    cnae_text2 = ativ2[cont]['text'].replace(",",";")
                else:
                    cnae_cod2 = cnae_cod2 + ',' + ativ2[cont]['code'].replace(",",";")
                    cnae_text2 = cnae_text2 + ',' + ativ2[cont]['text'].replace(",",";")
                cont = cont + 1

            lista_dados.append(
                [
                    dado['cnpj'],
                    dado['nome'],
                    # dado['numero'],
                    # dado['complemento'],
                    dado['cep'],
                    # dado['bairro'],
                    dado['municipio'],
                    dado['uf'],
                    # dado['email'],
                    # dado['telefone']
                    #cnae_cod1,
                    #cnae_text1,
                    #cnae_cod2,
                    #cnae_text2
                ]
            )
        except Exception as erro:
            lista_dados.append(
                [
                    'erro',
                    'erro',
                    'erro',
                    'erro',
                    'erro',
                    'erro'
                ]
            )
    #Pausa no cod devido limite de consulta de 3 CNPJs por min
    if loop >3:
        time.sleep(70)

    return lista_dados

diretorio = 'C:/Users/andremt/OneDrive - Votorantim/Documentos/Python/'

#Buscar xlsx com os CNPJs
nome_arquivo = 'Lista_CNPJ.xlsx'
endereco = diretorio + nome_arquivo
total_cnpj = importar_csv(endereco)

#Arquivo que retornará valores da consulta
nome_arquivo = 'CNPJs.txt'
endereco = diretorio + nome_arquivo
cria_arquivo(endereco)

lista_cnpj = []
i=0

while i <= len(total_cnpj):
    lista_cnpj = total_cnpj[i:i+3]
    i += 3
    print(lista_cnpj)
    lista_dados = api_cnpj(lista_cnpj, len(total_cnpj))
    j=0
    for j in range(len(lista_dados)):
        atualizar_arquivo(endereco, lista_dados[j])