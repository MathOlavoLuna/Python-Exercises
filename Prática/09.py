from random import randint
from time import sleep


def vV(lista):
    global soma
    for n in lista:
        soma += n
    return soma

def vD(Lista):
    global soma1
    for n in Lista:
        soma1 += n
    return soma1

def VitoriaDerrota(x, y):
    if x > y:
        print('Você Ganhou a partida, Parabéns!!!')
    else:
        print('Você Perdeu a partida, tente novamente na proxima vez')


soma = 0
soma1 = 0
p = 0
v = 0
resultadov = []
resultadoD = []
continua = True
print('-=' * 15)
print('        JOKENPÔ GAME!!')
print('-=' * 15)
while continua:
    computador = randint(1, 3)
    print('1 - Pedra')
    sleep(0.4)
    print('2 - Papel')
    sleep(0.4)
    print('3 - Tesoura')
    sleep(0.4)
    print('-=' * 15)
    print('Qual sua jogada?')
    esco = int(input('ESCOLHA: '))
    if esco == 0:
        continua = False
    elif esco == 1 and computador == 2:
        print('Perdeu')
        p += 1
        resultadoD.append(p)

    elif esco == 2 and computador == 3:
        print('Perdeu')
        p += 1
        resultadoD.append(p)

    elif esco == 3 and computador == 1:
        print('Perdeu')
        p += 1
        resultadoD.append(p)

    elif esco == computador:
        print('Empate')

    else:
        print('Venceu')
        v += 1
        resultadov.append(v)

vV(resultadov)
vD(resultadoD)
VitoriaDerrota(soma, soma1)
