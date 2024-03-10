preco = float(input('Qual o preço do seu produto: '))
print('Como quer pagar?')
print('OPÇÃO 1: À vista')
print('OPÇÃO 2: Em 3x')
print('OPÇÃO 3: Em 5x')
print('OPÇÃO 4: Em 10x')
op = int(input('Local de escolha: '))
print('')
print('')
print('')
if op == 1:
    a = preco * 0.05
    t = preco - a
    print(f'Pagando à vista o preço final é igual a {t:.2f}R$')
elif op == 2:
    a = preco / 3
    print(f'Pagando em três vezes o preço final é igual a {preco:.2f}R$ e cada parcela custará {a:.2f}R$ por mês.')
elif op == 3:
    a = preco * 0.02
    t = preco + a
    p = t / 5
    print(f'Pagando em cinco vezes o preço final tem um aumento de {a:.2f}R$, totalizando {t:.2f}R$,')
    print(f'por cinco mêses você terá que pagar {p:.2f}R$')
elif op == 4:
    a = preco * 0.08
    t = preco + a
    p = t / 10
    print(f'Pagando em dez vezes o preço final tem um aumento de {a:.2f}R$, totalizando {t:.2f}R$,')
    print(f'por dez mês você terá que pagar {p:.2f}R$')
