soma = 0
qtd = 0
for p in range(1, 101):
    if (p % 2 == 0):
        soma += p
        qtd += 1
media = soma / qtd
print(f'A média entre os números pares entre 1 e 100 é igual a {media}')
