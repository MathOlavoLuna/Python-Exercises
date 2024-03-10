from time import sleep


def contagem(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if f < i:
        p *= -1
    for c in range(i, f+1, p):
        print(c, end=' ')
        sleep(0)
    print('FIM!')
    print('-=' * 15)



print(f'Contagem de 1 até 10 de 1 em 1')
contagem(1, 10, 1)
print(f'Contagem de 10 até 0 de 2 em 2')
contagem(10, -2, -2)

print('Agora é usa vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c2 = int(input('Passo: '))
contagem(a, b, c2)
