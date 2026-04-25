from lib.interface import *
from lib.interface.ferramentas import *
from lib import * 
from time import sleep
arq = 'CursoEmVideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com Sucesso!')
else:
    print('Arquivo não encontrado, criando um novo arquivo...')
    criarArquivo(arq)


while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
        verPessoasCadastradas(arq)
    elif resposta == 2:
        cabecalho('Opção 2')
        nome = str(input('Digite o Nome da pessoa: '))
        idade = leiaInt('Digite sua idade: ')
        if idade > 80:
            print("Idade invalida, tente novamente.")
        else:
            cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('\033[36mSaindo do sistema, até mais.\033[m')
        break
    else:
        print('ERRO: Digite um Valor válido')
    sleep(2)