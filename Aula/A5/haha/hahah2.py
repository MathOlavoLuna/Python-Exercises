def valida_int(pergunta, min , max):
    x = (pergunta)
    while x < min or x > max:
        return True
    else:
        return False


def espa():
    print('-=' * 15)


def CadastraG(lista, Jogo, Console):
    a = open(lista, 'at')

    try:
        a.write(f'{Jogo}; {Console}\n')

    except:
        print('Erro ao escrever no arquivo.')

    finally:
        a.close()


def Listar(lista):
    a = open(lista, 'rt')

    try:
        print(a.read())
    except:
        print('Não foi possivel exibir a lista')

    finally:
        a.close()


print('        COLEÇÃO GAMER')
arquivo = 'listo.txt'
open(arquivo, 'at+')
esco = False
while True:
    valida_int(esco, 1, 3)
    espa()
    print('             MENU')
    espa()
    print('1 - Cadastrar Jogo na Coleção')
    print('2 - Listar Jogos da Coleção')
    print('3 - Sair da Coleção')
    esco = int(input('Escolha: '))
    if esco == 1:
        espa()
        print('Cadastrando novo jogo...')
        x = str(input('Jogo: '))
        y = str(input('Console: '))
        CadastraG(arquivo, x, y)

    elif esco == 2:
        Listar(arquivo)

    if esco == 3:
        break
