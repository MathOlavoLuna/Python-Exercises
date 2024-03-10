print('Digite [ 1 ] para maçãs')
print('Digite [ 2 ] para laranjas')
print('Digite [ 3 ] para bananas ')
esco = int(input('Escolha: '))
if esco == 1:
    m = int(input('Quantas maçãs você quer comprar? '))
    total = 2.30 * m
    print(f'Comprando {m} maçãs o total a pagar é de {total:.2f}R$')

elif esco == 2:
    l = int(input('Quantas laranjas você quer comprar? '))
    total = 3.60 * l
    print(f'Comprando {l} laranjas o total a pagar é de {total:.2f}R$')
elif esco == 3:
    b = int(input('Quantas bananas você quer comprar? '))
    total = 1.85 * b
    print(f'Comprando {b} bananas o total a pagar é de {total:.2f}R$')
else:
    print('ERRO')