while True:
    idade = int(input('Digite sua idade: '))
    if idade < 0:
        break
    sexo = str(input('Qual seu sexo? [F/M]'))
    if sexo == 'F':
        print(f'Boa noite Senhora. Sua idade é {idade} anos')
    elif sexo == 'M':
        print(f'Boa noite Senhor. Sua idade é {idade} anos')