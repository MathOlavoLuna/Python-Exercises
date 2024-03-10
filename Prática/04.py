#Ex: 1 Aula prática: 4
print(' ')
print('Você deseja...')
print('Somar [+]')
print('Subtrair [-]')
print('Dividir [/]')
print('Multiplicar [*]')
print('Sair[S]')
esco = ''
while esco != '+' or esco != '-' or esco != '/' or esco != '*' or esco != 'S':
    print('=-' * 20)
    esco = str(input('Escolha um dos símbolos ENTRE os colchetes: '))
    if esco == 'S':
        break
    else:
        x = float(input('Digite 1ª Valor: '))
        y = float(input('Digite 2ª Valor: '))
        print(' ')
        if esco == '+':
            calc = int(x + y)
            print(f'A soma entre {x:.0f} e {y:.0f} é igual a {calc}')
            print(' ')

        elif esco == '-':
            calc = int(x - y)
            print(f'A subtração entre {x:.0f} e {y:.0f} é igual a {calc}')
            print(' ')
        elif esco == '/':
            calc = x / y
            print(f'A divisão entre {x:.0f} e {y:.0f} é igual a {calc:.2f}')
            print(' ')
        elif esco == '*':
            calc = x * y
            print(f'A multiplicação entre {x:.0f} e {y:.0f} é igual a {calc:.1f}')
            print(' ')
        print('Caso queira sair da calculadora digite: S ')
