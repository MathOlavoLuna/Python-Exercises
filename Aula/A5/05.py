def pi(x):
    if x % 2 == 0:
        return 'par'
    else:
        return 'ímpar'


a = int(input('Digite um número inteiro: '))
print(pi(a))
