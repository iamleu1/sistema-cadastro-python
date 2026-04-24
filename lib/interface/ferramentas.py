from lib import * 

def arquivoExiste(nome):
    try:
        with open(nome, 'rt') as a:
            return True
    except FileNotFoundError:
        return False

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
        a.write(f'{nome};{idade}\n')
    except:
        print('Houve um erro ao escrever os dados!')
    else:
        print(f'{nome} adicionado com sucesso!')
        a.close()

def verPessoasCadastradas(arq):
    try:
        a = open(arq, 'r')
    except FileNotFoundError:
        print('Não foi possivel abrir o arquivo.')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<5}{dado[1]:>3} anos')
    finally:
            a.close()

