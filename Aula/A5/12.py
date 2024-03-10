def valida_int(n, min, max):
    if n < min or n > max:
        return True
    else:
        return False


def fatorial(n1):
    """
    Função para calcular o fatorial.

    :param n1: Número que você deseja fatorar.
    :return: retorna o valor total da fatoração.

    """
    f = 1
    cont = n1
    print(f'{n1}! é igual: ')

    while cont >= 1:
        print(f'{cont}', end='')
        print(' x ' if cont > 1 else ' = ', end='')
        f *= cont
        cont -= 1

    return f


print('Entre 1/10')
x = int(input('Quer saber o fatorial de que número?: '))
while valida_int(x, 1, 10):
    print('Entre 1/10')
    x = int(input('Quer saber o fatorial de que número?: '))
print(fatorial(x))
