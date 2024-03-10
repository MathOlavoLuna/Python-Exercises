def cadastraPeca(código):
    global cont
    print('Você Selecionou a Opção de Cadastrar Peça')
    a = código
    peças['Código'] = a
    print(f'Código da Peça 00{a}')
    peças['Nome'] = str(input('Qual o nome da Peça: '))
    peças['Fabricante'] = str(input('Qual o Fabricante da Peça: '))
    peças['Valor'] = float(input('Qual o valor da Peça: '))
    peçaStack.append(peças.copy())
    cont += 1


def consultarPeca():
    while True:
        print('Você Selecionou a Opção Consultar Peças')
        print('Escolha a opção desejada:')
        print('1 - Consultar Todas as Peças')
        print('2 - Consultar Peças por Código')
        print('3 - Consultar Peças por Fabricante')
        print('4 - Sair')
        consulta = int(input('>> '))
        if consulta == 1:
            for i in peçaStack:
                print('*' * 15)
                for j, x in i.items():
                    print(f'{j} : {x}')
            print('*' * 15)
            print()
        elif consulta == 2:
            coc = int(input('Digite o Código da Peça: '))
            print('*' * 15)
            for i, v in peçaStack[coc - 1].items():
                print(f'{i} : {v}')
            print('*' * 15)
        elif consulta == 3:
            f = str(input('Digite o nome do FABRICANTE: '))
            for i in peçaStack:
                print('*' * 15)
                for c in i.values():
                    if c == f:
                        for i, v in i.items():
                            print(f'{i} : {v}')
            print('*' * 15)
        elif consulta == 4:
            return


def removerPeca():
    global cont
    print('Você selecionou a Opção de Remover Peça')
    coc = int(input('Digite o Código da Peça a ser removida: '))
    try:
        del peçaStack[coc - 1]
    except:
        del peçaStack[coc]
        print('Você tem menos de um produto no carrinho')
    finally:
        print('Sucesso')
        cont -= 1

# Programa Princípal
cont = 1
peças = {}
peçaStack = []
while True:
    print('Bem Vindo ao Controle de Estoque da Bicicletaria do Matheus Olavo Marques Luna')
    print('Escolha a opção desejada:')
    print('1 - Cadastras Peças')
    print('2 - Consultar Peças')
    print('3 - Remover peças')
    print('4 - Sair')
    escolha = int(input('>> '))
    if escolha == 1:
        cadastraPeca(cont)
        continue
    elif escolha == 2:
        consultarPeca()
    elif escolha == 3:
        removerPeca()
    elif escolha == 4:
        break

