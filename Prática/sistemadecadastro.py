def cads(nome, idade, lista):
    b = definitivo['nome'] = nome
    c = definitivo['idade'] = idade
    personas.append(definitivo.copy())
    try:
        a = open(lista, 'at')
        a.write(f'{definitivo["nome"]} de {definitivo["idade"]} Anos\n')
    except:
        print('deu erro garai')
    finally:
        a.close()
        print('Cadastrando usuário...')
        print()


def abrelista(lista):
    try:
        print('Mostrando Usuários Cadastrados...')
        print()
        a = open(lista, 'rt')
        print(a.read())
    except:
        print('deu erro garai')
    finally:
        a.close()



#programa principal
personas = []
definitivo = {}
a = 'lista.txt'
esco = 0
while True:
    print('-' * 20)
    print('MENU')
    print('-' * 20)
    print('1 - Cadastrar nova pessoa')
    print('2 - Listar pessoas cadastradas')
    print('3 - Sair do programa')
    esco = int(input('Escolha: '))
    if esco == 1:
        x = str(input('Digite seu nome: '))
        y = int(input('Digite sua idade: '))
        cads(x, y, a)
    if esco == 2:
        abrelista(a)
    if esco == 3:
        break
