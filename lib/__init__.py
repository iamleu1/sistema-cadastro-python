def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR:\033[m \033[32mIsso\033[m \033[33mnão \033[34mé\033[m \033[35muma\033[m \033[36mresposta\033[m \033[37mválida.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mERROR: usuario não digitou este campo.\033[m')
            return 0
        else:
            return n

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('\033[37mMenu Principal\033[m')
    c = 1
    print(linha())
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[35mSua Opção: \033[m')
    return opc

def criarArquivo(nome):
    try:
        with open(nome, 'wt+') as a:
            pass
    except:
        print('\033[31mERROR: arquivo já existe.\033[m')
    else:
        print(f'\033[32mArquivo {nome} criado com Sucesso!\033[m')
    
    