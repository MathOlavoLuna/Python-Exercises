def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x


def fatorial(num):
    fac = 1
    if num == 0:
        return fac
    for f in range(1, num+1, 1):
        fac *= f
    return fac


x = valida_int('Digite um número para calcular o fatorial: ', 1, 10)
print(f'{x}! = {fatorial(x)}')
