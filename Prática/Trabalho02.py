print('Bem vindo a Lanchonete do Matheus Olavo Marques Luna')
print('*' * 15, 'Cardápio', '*' * 15)
print('|  Código  |        Descrição        |  Valor  |')
print('|    100   |     Cachorro Quente     |   9,00  |')
print('|    101   |  Cachorro Quente Duplo  |  11,00  |')
print('|    102   |           X-Egg         |  12,00  |')
print('|    103   |         X-Salada        |  12,00  |')
print('|    104   |          X-Bacon        |  14,00  |')
print('|    105   |          X-Tudo         |  17,00  |')
print('|    200   |    Refrigerante Lata    |   5,00  |')
print('|    201   |        Chá Gelado       |   4,00  |')

total = 0  # Calcula o valor para ser pago no fim.
continua = True  # Para ficar repetindo.
código = 202  # Deixei o código negado já para já cair num laço de repetição.

while continua:  # Enquanto continua for verdadeiro o programa fica em loop.
    código = int(input('Entre com o código desejado: '))

    if código != 100 and código != 101 and código != 102 and código != 103 and código != 104 and código != 105 and código != 200 and código != 201:
        print('Opção Inválida')
        continue
        # Esse if verifica se o número é diferente de algum dos números da tabela, acho que dá para fazer de uma forma
        # mais dinâmica, mas foi do jeito que deu no momento, sinceramente nem sei porque o and funcionou ao ínves do or.

    else:  # se não cair no if, o programa continua.
        if código == 100:
            print('Você pediu um Cachorro Quente no valor de R$: 9,00')
            total += 9

        elif código == 101:
            print('Você pediu um Cachorro Quente Duplo no valor de R$: 11,00')
            total += 11

        elif código == 102:
            print('Você pediu um X-Egg no valor de R$: 12,00')
            total += 12

        elif código == 103:
            print('Você pediu um X-Salada no valor de R$: 12,00')
            total += 12

        elif código == 104:
            print('Você pediu um X-Bacon no valor de R$: 14,00')
            total += 14

        elif código == 105:
            print('Você pediu um X-Tudo no valor de R$: 17,00')
            total += 17

        elif código == 200:
            print('Você pediu um Refrigerante Lata no valor de R$: 5,00')
            total += 5

        elif código == 201:
            print('Você pediu um Chá Gelado no valor de R$: 4,00')
            total += 4

        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('0 - Não')
        decisão = int(input('>> '))

        if decisão == 1:  # if que verifica se a decisão de continuar comprando é sim ou não.
            continue
        elif decisão == 0:
            continua = False
print(f'O total a ser pago é: {total:.2f}')


