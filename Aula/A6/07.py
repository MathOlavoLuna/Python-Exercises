#Ex 06 só que de outra forma:
mercado = []

for i in range(3):
    nome = input('Digite o nome do item: ')
    qtd = input('Digite a quantidade: ')
    valor = float(input('Digite o valor: '))
    mercado.append([nome, qtd, valor])
print('  Produto  |  Quantia  |  Valor  ')
print(f'  {mercado[0][0]}  |  {mercado[0][1]}  |  {mercado[0][2]}  ')
print(mercado[1][0], mercado[1][1], mercado[1][2] )
print(mercado[2][0], mercado[2][1], mercado[2][2] )