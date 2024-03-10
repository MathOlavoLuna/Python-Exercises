from time import sleep
def valida_int(n, min, max):
    if n < min or n > max:
        return True
    else:
        return False


def espa():
    print('~' * 22)


def CadatrarNi(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir arquivo')
    else:
        a.write(f'{nomeJogo};{nomeVideogame}\n')
    finally:
        a.close()


def MostrarItens(coleção):
    a = open(coleção, 'rt')
    try:
        print(a.read())
    except:
        print('Erro ao exibir a coleção')
    finally:
        a.close()

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação da coleção de jogos')
    else:
        print('Sua coleção foi criada')


def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# programming
arquivo = "lista.txt"
if existeArquivo(arquivo):
    print('Coleção de jogos existente')
else:
    print('Coleção de jogos inexistente')
    criaArquivo(arquivo)

while True:
    sleep(0.45)
    espa()
    print('         MENU')
    espa()
    print('1 - Cadastra Novo Jogo')
    print('2 - Listar Jogos')
    print('3 - Sair')
    espa()
    sleep(0.5)
    esco = int(input("ESCOLHA: "))

    while valida_int(esco, 1, 3):
        esco = int(input("ESCOLHA: "))

    if esco == 1:
        sleep(0.5)
        print('Cadastrando novo jogo')
        espa()
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do Videogame: ')
        CadatrarNi(arquivo, nomeJogo, nomeVideogame)

    elif esco == 2:
        sleep(0.5)
        print('Lista de jogos na coleção')
        espa()
        MostrarItens(arquivo)

    elif esco == 3:
        frase = 'Encerrando programa.'
        for l in range(0, len(frase), 1):
            print(frase[l], end='')
            sleep(0.25)
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        break
