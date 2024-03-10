def dimensõesObjeto():
    while True:
        try:
            a = float(input('Qual a altura do objeto em (cm): '))
            b = float(input('Qual o comprimento do objeto em (cm): '))
            c = float(input('Qual a largura do objeto em (cm): '))

        except ValueError:
            print('As dimensões do objeto só podem ser representadas por números!')
            print('Porfavor digite as dimensões novamente.')
            continue
        else:
            volume = a * b * c #Calcula o volume
            if volume < 1000:
                valor = 10
                return valor

            elif volume < 10000:
                valor = 20
                return valor

            elif volume < 30000:
                valor = 30
                return valor


            elif volume < 100000:
                valor = 50
                return valor

            elif volume > 100000:
                print('Não transprotamos objetos tão desse temanho')
                continue
            break

def pesoObjeto():
    while True:
        try:
            p = float(input('Qual o peso do objeto em (kg): '))

        except ValueError:
            print('O peso do objeto só podem ser representado por números!')
            print('Porfavor digite o peso novamente.')

        else:
            if p <= 0.1:
                multi = 1
                return multi

            elif p <= 1:
                multi = 1.5
                return multi

            elif p < 10:
                multi = 2
                return multi

            elif p < 30:
                multi = 3
                return multi

            elif p >= 30:
                print('Não aceitamos objetos tão pesados.')
                continue
            break


def rotaObjeto():
    print('Selecione a rota: ')
    print(' BR - De Brasília para Rio de Janeiro')
    print(' BS - De Brasília para São Paulo')
    print(' RB - De Rio de Janeiro para Brasília')
    print(' RS - De Rio de Janeiro para São Paulo')
    print(' SR - De São Paulo para Rio de Janeiro')
    print(' SB - De São Paulo para Brasília')
    while True:
        pr = str(input('>> '))
        if pr not in 'BR RB BS SB RS SR':  # Se o conteudo da variável pr não estiver entre BR RB BS SB etc.. o programa fica em loop
            print('Você digitou uma rota não existente.')
            continue
        else:
            if pr == 'BR' or pr == 'RB':
                mR = 1.5
            if pr == 'BS' or pr == 'SB':
                mR = 1.2
            if pr == 'RS' or pr == 'SR':
                mR = 1
            return mR  # multiRota
            break


# Programa príncipal
print('Bem vindo a Companhia de Logística Matheus Olavo Marques Luna S.A. ')
valorV = dimensõesObjeto()
multiPeso = pesoObjeto()
multiRota = rotaObjeto()

total = valorV * multiPeso * multiRota  # Calcula o valor a ser cobrado
print(f'Total a pagar R$:{total:.2f} (dimensão: {valorV} * peso: {multiPeso} * rota: {multiRota})')
