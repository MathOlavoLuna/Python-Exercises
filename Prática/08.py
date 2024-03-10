t10 = ('Arroz', 'Lógica', 'Mouse', '8BitDo', 'Xbox', 'E-Yooso',
       'Valorant', 'Superações', 'Vínicius', 'Gabusborn')

for anda in t10:
    print(f'\nPalavra: {anda}. Vogais: ', end='')
    for l in anda:
        if l in 'aAeEiIoOuU':
            print(l, end=' ')
