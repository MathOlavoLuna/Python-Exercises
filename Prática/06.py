print('=-' * 15)
print('CINE LUNA')
print('=-' * 15)
p = 0
total = 0
sex = 0
while True:
    idade = input('Qual sua idade?: ')
    if idade == "S":
        break

    idade = int(idade)
    if idade < 3:
        ing = 0
    else:
        if idade > 12:
            ing = 30
        else:
            ing = 15
    total += ing
    sex += idade
    p += 1
    print('=-' * 15)
mediaI = sex / p
print(f'Você comprou  {p} ingressos, totalizando {total:.2f}R$.')
print(f'A média da idade entre as pessoas é de {mediaI} anos')

