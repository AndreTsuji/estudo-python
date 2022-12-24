import shutil


def escrever_arquivo(endereco, texto):
    # Criar um arquivo
    arquivo = open(endereco, 'w')

    # Nova escrita
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(endereco, texto):
    arquivo = open(endereco, 'a')
    arquivo.write('\n' + texto)
    arquivo.close()


def ler_arquivo(endereco):
    arquivo = open(endereco, 'r')
    texto = arquivo.read()
    print(texto)


def media_notas(endereco):
    arquivo = open(endereco, 'r')
    lista_media = []

    # split: Converte a string em uma lista
    aluno_nota = arquivo.read().split('\n')
    for x in aluno_nota:
        lista_notas = x.split(',')
        # aluno recebe apenas o primeiro elemento da lista (nome)
        aluno = lista_notas[0]
        # remove o primeiro elemento(nome) da lista, restando apenas as notas
        lista_notas.pop(0)
        # função lamdba que calcula média
        def media(notas): return sum([int(i) for i in notas]) / 4
        lista_media.append({aluno: media(lista_notas)})
    return lista_media


def copia_arquivo(endereco):
    shutil.copy(
        endereco, 'C:/Users/tsuji/OneDrive/Documentos/André/Python/Aulas')


def move_arquivo(endereco):
    shutil.move(
        endereco, 'C:/Users/tsuji/OneDrive/Documentos/André/Python/Aulas')


if __name__ == '__main__':

    # define diretório para função open
    diretorio = 'C:/Users/tsuji/OneDrive/Documentos/André/Python/Aulas/Introducao_Python'
    nome_arquivo = 'alunos.txt'
    endereco = diretorio + nome_arquivo

    # aluno = 'Cesar,7,9,3,8'
    # escrever_arquivo(endereco, aluno)
    # atualizar_arquivo(endereco, aluno)
    # ler_arquivo(endereco)
    lista_media = media_notas(endereco)
    print(lista_media)
