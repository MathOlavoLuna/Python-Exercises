preco = float(input('Qual o valor do produto?: '))
d = float(input('Qual a porcentagem de desconto?: '))
desconto = preco * (d / 100)
pf = preco - desconto
print(f'O Desconto aplicado foi  de {desconto:.2f}R$ e o preço final do produto foi de {preco:.2f}R$ -> {pf:.2f}R$ ')